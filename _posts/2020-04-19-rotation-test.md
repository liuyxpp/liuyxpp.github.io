---
layout: post
title: "Usage and Testing of rotation.jl"
subheadline: "A Julia notebook"
description: "Numerical experiments are carried out to demonstrate the usage as well as serving as a test for the rotation.jl submodule."
author: lyx
date: 2020-04-19
modified: 2020-04-19
image:
    feature: false
    twitter: false
categories: [Software, Tutorial]
tags: [Julia, Scattering.jl, test]
show_meta:
    info: true
---

Numerical experiments are carried out to demonstrate the usage as well as serving as a test for the `rotation.jl` submodule. This is an appendix to the [previous post]({% post_url 2020-04-18-scattering-4 %}).

<!--more-->

{% include toc.md panel=true %}

First, we load some necessary packages

```julia
using Revise
using Scattering
using LinearAlgebra
using Test
```

## Some Experiments on Rotation Operations

$\vu, \vv, \vw$ are the basis vectors of the UVW internal coordinate system with their components expressed in the reference XYZ coordinate system. Let $\vw$ point to the principle direction of a scatterer.

```julia
w = [1.0, 2.0, 3.0]
normalize!(w)
# pick a vector that is not parallel to w
a = [0, 1, 2]
# find u by cross product
u = cross(w, a)
normalize!(u)
# find v perpendicular to both w and u
v = cross(w, u)
normalize!(v)
w
```

```
3-element Array{Float64,1}:
 0.2672612419124244
 0.5345224838248488
 0.8017837257372732
```

$\mP$ is the rotation matrix which rotates XYZ coordinate system (basis vectors) to UVW coordinate system: $[\vu\;\vv\;\vw] = [\ve_x\;\ve_y\;\ve_z]\mP$.

```julia
P = hcat(u, v, w)
```

```
3×3 Array{Float64,2}:
  0.408248   0.872872  0.267261
 -0.816497   0.218218  0.534522
  0.408248  -0.436436  0.801784
```

$\mR$ is the rotation matrix which rotates a vector in XYZ system to UVW coordinate system: $\mR = \mP^{-1} = \mP^T$ and $\mR\vu = [1\;0\;0]^T, \mR\vv = [0\;1\;0]^T, \mR\vw = [0\;0\;1]^T$

```julia
@test transpose(P) ≈ inv(P)
R = transpose(P)
```

```
3×3 LinearAlgebra.Transpose{Float64,Array{Float64,2}}:
 0.408248  -0.816497   0.408248
 0.872872   0.218218  -0.436436
 0.267261   0.534522   0.801784
```

```julia
@test det(R) ≈ 1
```

```
Test Passed
```

Verify that $\mR$ indeed transforms basis vectors of the XYZ coordinate system to $\vu, \vv, \vw$, whose components are expressed in the XYZ coordinate system.

```julia
@test R * u ≈ [1, 0, 0]
@test R * v ≈ [0, 1, 0]
@test R * w ≈ [0, 0, 1]
```

```
Test Passed
```

```julia
tr(R)
```

```
1.4282499064371286
```

Compute the rotation angle:

```julia
θ = acos((tr(R)-1)/2)
rad2deg(θ)
```

```
77.63580469304388
```

Compute the rotation axis expressed in the XYZ system:

```julia
uu = [R[3,2]-R[2,3], R[1,3]-R[3,1], R[2,1]-R[1,2]] / (2sin(θ))
```

```
3-element Array{Float64,1}:
 0.49700656431759865
 0.07216735383016143
 0.8647406247345901
```

Alternative way to compute the rotation axis. Note that the result may be different from the one computed above with only a sign.

```julia
vals, vecs = eigen(R)
idx = findfirst(x -> x ≈ one(x), vals)
uu2 = real(vecs[:, idx])
@test uu2 ≈ uu || uu2 ≈ -uu
```

```
Test Passed
```

Alternative way to compute the rotation angle

```julia
vv = [R[3,2]-R[2,3], R[1,3]-R[3,1], R[2,1]-R[1,2]]
@test asin(norm(vv)/2) ≈ θ
```

```
Test Passed
```

A proper rotation matrix should have $\det(\mR) = +1$

```julia
det(R)
```

```
1.0000000000000002
```

```julia
transpose(R)
```

```
3×3 Array{Float64,2}:
  0.408248   0.872872  0.267261
 -0.816497   0.218218  0.534522
  0.408248  -0.436436  0.801784
```

```julia
inv(R)
```

```
3×3 LinearAlgebra.Transpose{Float64,Array{Float64,2}}:
  0.408248   0.872872  0.267261
 -0.816497   0.218218  0.534522
  0.408248  -0.436436  0.801784
```

A proper rotation matrix should be an orthogonal matrix

```julia
@test transpose(R) ≈ inv(R)
```

```
Test Passed
```

Convert current rotation matrix representation to Euler angles representation. Convention used: Z1Y2Z3

Procedure:
1. Rotate about +z by eta (counter-clockwise in x-y plane),
2. Rotate about the former y-axis (which is y'), counter clockwise in x'-z plane. Then,
3. Rotate about the former z-axis (which is z'), counter-clockwise in x'-y' plane.

See wiki page:
1. https://en.wikipedia.org/wiki/Rotation_matrix
2. https://en.wikipedia.org/wiki/Euler_angles#Intrinsic_rotations

```julia
α = atan(R[2,3], R[1,3])
β = acos(R[3,3])
γ = atan(R[3,2], -R[3,1])
rad2deg.([α, β, γ])
c1 = cos(α)
c2 = cos(β)
c3 = cos(γ)
s1 = sin(α)
s2 = sin(β)
s3 = sin(γ)

Ra = zero(R)
Ra[1, 1] = c1*c2*c3 - s1*s3
Ra[1, 2] = -c3*s1 - c1*c2*s3
Ra[1, 3] = c1 * s2
Ra[2, 1] = c1*s3 + c2*c3*s1
Ra[2, 2] = c1*c3 - c2*s1*s3
Ra[2, 3] = s1*s2
Ra[3, 1] = -c3*s2
Ra[3, 2] = s2*s3
Ra[3, 3] = c2
@test Ra ≈ R
```

```
Test Passed
```

```julia
rad2deg.([α, β, γ])
```

```
3-element Array{Float64,1}:
 -46.91127686463718
  36.69922520048988
 116.56505117707799
```

Convention: Z1X2Z3

```julia
α = atan(R[1,3], -R[2,3])
β = acos(R[3,3])
γ = atan(R[3,1], R[3,2])
rad2deg.([α, β, γ])
c1 = cos(α)
c2 = cos(β)
c3 = cos(γ)
s1 = sin(α)
s2 = sin(β)
s3 = sin(γ)

Rb = zero(R)
Rb[1, 1] = c1*c3 - c2*s1*s3
Rb[1, 2] = -c1*s3 - c2*c3*s1
Rb[1, 3] = s1 * s2
Rb[2, 1] = c3*s1 + c1*c2*s3
Rb[2, 2] = c1*c2*c3 - s1*s3
Rb[2, 3] = -c1*s2
Rb[3, 1] = s2*s3
Rb[3, 2] = c3*s2
Rb[3, 3] = c2
@test Rb ≈ R
```

```
Test Passed
```

Convention Z1Y2X3

```julia
α = atan(R[2,1],R[1,1])
β = asin(-R[3,1])
γ = atan(R[3,2], R[3,3])
rad2deg.([α, β, γ])
c1 = cos(α)
c2 = cos(β)
c3 = cos(γ)
s1 = sin(α)
s2 = sin(β)
s3 = sin(γ)

Z1Y2X3 = zero(R)
Z1Y2X3[1, 1] = c1*c2
Z1Y2X3[1, 2] = c1*s2*s3 - c3*s1
Z1Y2X3[1, 3] = s1*s3 + c1*c3*s2
Z1Y2X3[2, 1] = c2*s1
Z1Y2X3[2, 2] = c1*c3 + s1*s2*s3
Z1Y2X3[2, 3] = c3*s1*s2 - c1*s3
Z1Y2X3[3, 1] = -s2
Z1Y2X3[3, 2] = c2*s3
Z1Y2X3[3, 3] = c2*c3
@test Z1Y2X3 ≈ R
```

```
Test Passed
```

Convention: Z1Y2Z3

```julia
Rp = hcat([-1, 0, 0], [0, 0, 1], [0, 1, 0])
α = atan(Rp[2,3], Rp[1,3])
β = acos(Rp[3,3])
γ = atan(Rp[3,2], -Rp[3,1])
rad2deg.([α, β, γ])

θp = acos((tr(Rp)-1)/2)
up =[Rp[3,2]-Rp[2,3], Rp[1,3]-Rp[3,1], Rp[2,1]-Rp[1,2]]
θpp = asin(norm(up)/2)
```

```
0.0
```

```julia
rad2deg(θp), rad2deg(θpp), up
```

```
(180.0, 0.0, [0, 0, 0])
```

Find rotation axis by diagonalization

```julia
vals, vecs = eigen(Rp)
idx = findfirst(x -> x ≈ one(x), vals)
uu = real(vecs[:, idx])
```

```
3-element Array{Float64,1}:
 0.0
 0.7071067811865475
 0.7071067811865477
```

## Testing and Usage of Scattering/rotation.jl

### Testing EulerAngle constructors

```julia
using StaticArrays: SVector, FieldVector
α, β, γ = π/4, π/3, π/2
```

```
(0.7853981633974483, 1.0471975511965976, 1.5707963267948966)
```

Constructors of `EulerAngle`. Initialize by a vector

```julia
EulerAngle([α, β, γ])
```

```
Scattering.Rotation.EulerAngle{Float64}(0.7853981633974483, 1.0471975511965976, 1.5707963267948966)
```

```julia
EulerAngle(1.3, 0, 0)
```

```
Scattering.Rotation.EulerAngle{Float64}(1.3, 0.0, 0.0)
```

Initialize by three angles

```julia
euler = EulerAngle(α, β, γ)
```

```
Scattering.Rotation.EulerAngle{Float64}(0.7853981633974483, 1.0471975511965976, 1.5707963267948966)
```

Copy constructor

```julia
EulerAngle(euler)
```

```
Scattering.Rotation.EulerAngle{Float64}(0.7853981633974483, 1.0471975511965976, 1.5707963267948966)
```

Initialize by a static vector

```julia
sv = SVector(1.0, 2.0, 3.0)
EulerAngle(sv)
```

```
Scattering.Rotation.EulerAngle{Float64}(1.0, 2.0, 3.0)
```

Follow the Z1Y2Z3 convention

```julia
α = atan(v[3], u[3])
β = acos(w[3])
γ = atan(w[2], -w[1])
rad2deg.([α, β, γ])
```

```
3-element Array{Float64,1}:
 -46.91127686463718
  36.69922520048988
 116.56505117707799
```

### Testing RotationMatrix constructors

Constructor of `RotationMatrix` initialized with a matrix

```julia
rotmat = RotationMatrix(Vector3D(u), Vector3D(v), Vector3D(w))
@test transpose(RotMatrix(hcat(u,v,w))) ≈ rotmat.R
```

```
Test Passed
```

Convert an `EulerAngle` instance to a `RotationMatrix` instance

```julia
rotmat_euler = RotationMatrix(EulerAngle(α, β, γ))
@test rotmat_euler.R ≈ rotmat.R
```

```
Test Passed
```

Convert a `RotationMatrix` instance to an `EulerAngle` instance

```julia
euler = EulerAngle(rotmat_euler)
@test [euler.α, euler.β, euler.γ] ≈ [α, β, γ]
```

```
Test Passed
```

### Testing EulerAxisAngle Constructors

Constructor of `AxisAngleRepresentation` initialized with a `RotationMatrix` instance: conversion from rotation matrix representation to axis-angle representation

```julia
axisangle = EulerAxisAngle(rotmat)
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([0.49700656431759865, 0.07216735383016143, 0.8647406247345901], 1.3550004093288814, [0.0 -0.8647406247345901 0.07216735383016143; 0.8647406247345901 0.0 -0.49700656431759865; -0.07216735383016143 0.49700656431759865 0.0])
```

Convert Euler axis-angle representation to rotation matrix representation

```julia
rotmat_axisangle = RotationMatrix(axisangle)
@test rotmat_axisangle.R ≈ rotmat.R atol=1e-15
```

```
Test Passed
```

```julia
axisangle2 = EulerAxisAngle(axisangle.ω, axisangle.θ)
@test axisangle2.K ≈ axisangle.K
```

```
Test Passed
```

### Testing conversion and promotion

```julia
euler
```

```
Scattering.Rotation.EulerAngle{Float64}(-0.8187562376025611, 0.6405223126794245, 2.0344439357957027)
```

```julia
axisangle
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([0.49700656431759865, 0.07216735383016143, 0.8647406247345901], 1.3550004093288814, [0.0 -0.8647406247345901 0.07216735383016143; 0.8647406247345901 0.0 -0.49700656431759865; -0.07216735383016143 0.49700656431759865 0.0])
```

```julia
EulerAxisAngle(euler)
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([0.4970065643175987, 0.07216735383016142, 0.86474062473459], 1.3550004093288814, [0.0 -0.86474062473459 0.07216735383016142; 0.86474062473459 0.0 -0.4970065643175987; -0.07216735383016142 0.4970065643175987 0.0])
```

```julia
RotationMatrix(euler) |> EulerAxisAngle
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([0.4970065643175987, 0.07216735383016142, 0.86474062473459], 1.3550004093288814, [0.0 -0.86474062473459 0.07216735383016142; 0.86474062473459 0.0 -0.4970065643175987; -0.07216735383016142 0.4970065643175987 0.0])
```

```julia
EulerAngle(axisangle)
```

```
Scattering.Rotation.EulerAngle{Float64}(-0.8187562376025609, 0.6405223126794247, 2.0344439357957027)
```

```julia
convert(EulerAngle, axisangle)
```

```
Scattering.Rotation.EulerAngle{Float64}(-0.8187562376025609, 0.6405223126794247, 2.0344439357957027)
```

```julia
convert(EulerAngle, euler)
```

```
Scattering.Rotation.EulerAngle{Float64}(-0.8187562376025611, 0.6405223126794245, 2.0344439357957027)
```

### Testing promotion, comparison, and unit rotation

```julia
@test euler == axisangle
```

```
Test Passed
```

```julia
@test euler == euler
```

```
Test Passed
```

```julia
@test promote(euler) == rotmat
```

```
Test Passed
```

```julia
@test promote(axisangle) == rotmat
```

```
Test Passed
```

```julia
one(rotmat)
```

```
Scattering.Rotation.RotationMatrix{Float64}([1.0 0.0 0.0; 0.0 1.0 0.0; 0.0 0.0 1.0])
```

```julia
one(euler)
```

```
Scattering.Rotation.EulerAngle{Float64}(0.0, 0.0, 0.0)
```

```julia
promote(one(euler))
```

```
Scattering.Rotation.RotationMatrix{Float64}([1.0 -0.0 0.0; 0.0 1.0 0.0; -0.0 0.0 1.0])
```

```julia
one(axisangle)
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([1.0, 0.0, 0.0], 0.0, [0.0 -0.0 0.0; 0.0 0.0 -1.0; -0.0 1.0 0.0])
```

```julia
promote(one(axisangle))
```

```
Scattering.Rotation.RotationMatrix{Float64}([1.0 0.0 0.0; 0.0 1.0 0.0; 0.0 0.0 1.0])
```

### Testing inv function

```julia
rot1 = rotmat
```

```
Scattering.Rotation.RotationMatrix{Float64}([0.408248290463863 -0.816496580927726 0.408248290463863; 0.8728715609439696 0.21821789023599242 -0.4364357804719848; 0.2672612419124244 0.5345224838248488 0.8017837257372732])
```

Test `inv` function for `RotationMatrix`

```julia
irot1 = inv(rot1)
@test transpose(rot1.R) ≈ irot1.R
```

```
Test Passed
```

```julia
rot2 = EulerAxisAngle(rot1)
```

```
Scattering.Rotation.EulerAxisAngle{Float64}([0.49700656431759865, 0.07216735383016143, 0.8647406247345901], 1.3550004093288814, [0.0 -0.8647406247345901 0.07216735383016143; 0.8647406247345901 0.0 -0.49700656431759865; -0.07216735383016143 0.49700656431759865 0.0])
```

Test `inv` function for `EulerAxisAngle`

```julia
irot2 = inv(rot2)
@test irot2 == irot1
```

```
Test Passed
```

```julia
rot3 = EulerAngle(rot1)
```

```
Scattering.Rotation.EulerAngle{Float64}(-0.818756237602561, 0.6405223126794245, 2.0344439357957027)
```

Test `inv` function for `EulerAngle`

```julia
irot3 = inv(rot3)
@test irot3 == irot1
```

```
Test Passed
```

### Testing multiplication of two AbstractRotation instances

Test multiplication of two `RotationMatrix` instances.

```julia
R1 = rotmat
M = RotationMatrix(Rp)
R2 = R1 * M
@test R2.R ≈ R1.R*M.R
```

```
Test Passed
```

Test multiplication of a `EulerAxisAngle` instance and a `RotationMatrix` instance.

```julia
R1 = rotmat
R1a = EulerAxisAngle(R1)
M = RotationMatrix(Rp)
R2 = R1a * M
@test R2 == R1 * M
```

```
Test Passed
```

Test multiplication of a `RotationMatrix` instance and a `EulerAxisAngle` instance.

```julia
R1 = rotmat
M = RotationMatrix(Rp)
Ma = EulerAxisAngle(M)
R2 = R1 * Ma
@test R2 == R1 * M
```

```
Test Passed
```

Test multiplication of a `EulerAxisAngle` instance and a `EulerAxisAngle` instance.

```julia
R1 = rotmat
R1a = EulerAxisAngle(R1)
M = RotationMatrix(Rp)
Ma = EulerAxisAngle(M)
R2 = R1a * Ma
@test R2 == R1 * M
```

```
Test Passed
```

### Testing computing power of a AbstractRotation instance

```julia
function pow1(rot::AbstractRotation, n::Integer)
    rot = promote(rot)
    result = rot
    for i in 1:(n-1)
        result *= rot
    end
    result
end

function pow(rot::RotationMatrix, n::Integer)
    if n == zero(n)
        return one(rot)
    elseif n == one(n)
        return rot
    else
        if isodd(n)
            return rot * pow(rot, n-1)
        else
            rothalf = pow(rot, n÷2)
            return rothalf * rothalf
        end
    end
end

pow(rot::AbstractRotation, n::Integer) = pow(promote(rot), n)
```

```
pow (generic function with 2 methods)
```

```julia
pow(euler, 0)
```

```
Scattering.Rotation.RotationMatrix{Float64}([1.0 0.0 0.0; 0.0 1.0 0.0; 0.0 0.0 1.0])
```

```julia
pow(euler, 1)
```

```
Scattering.Rotation.RotationMatrix{Float64}([0.40824829046386313 -0.8164965809277259 0.4082482904638629; 0.8728715609439694 0.21821789023599242 -0.4364357804719848; 0.26726124191242434 0.5345224838248487 0.8017837257372732])
```

```julia
pow(euler, 2)
```

```
Scattering.Rotation.RotationMatrix{Float64}([-0.4369210333151354 -0.2932896043722907 0.8503418245705543; 0.43018214432212887 -0.8983623348886722 -0.08881687880007882; 0.7899641342195538 0.32699590703939707 0.5186813505672173])
```

```julia
pow(euler, 3)
```

```
Scattering.Rotation.RotationMatrix{Float64}([-0.20711300761088602 0.7472703153125533 0.6314200487243415; -0.6322711178708509 -0.5947556020638506 0.4964866637886771; 0.7465503570320742 -0.29639981387703873 0.5956590591512387])
```

```julia
pow(euler, 4)
```

```
Scattering.Rotation.RotationMatrix{Float64}([0.7364715816744584 0.6696830270043788 0.09557328459445946; -0.644577211376976 0.651844177986726 0.3995239494677259; 0.2052555187063243 -0.35584239624735736 0.9117271308201462])
```

```julia
pow(euler, 5).R
```

```
3×3 StaticArrays.SArray{Tuple{3,3},Float64,2,9} with indices SOneTo(3)×SOneTo(3):
 0.910754   -0.404104   0.0850187
 0.412606    0.882094  -0.227304
 0.0168598   0.242097   0.970106
```

```julia
pow(euler, 100).R
```

```
3×3 StaticArrays.SArray{Tuple{3,3},Float64,2,9} with indices SOneTo(3)×SOneTo(3):
 -0.443094   0.414668   0.794807
 -0.277188  -0.906518   0.318422
  0.852546  -0.0792197  0.516614
```

```julia
euler^1
```

```
Scattering.Rotation.RotationMatrix{Float64}([0.40824829046386313 -0.8164965809277259 0.4082482904638629; 0.8728715609439694 0.21821789023599242 -0.4364357804719848; 0.26726124191242434 0.5345224838248487 0.8017837257372732])
```

```julia
euler^2
```

```
Scattering.Rotation.RotationMatrix{Float64}([-0.4369210333151354 -0.2932896043722907 0.8503418245705543; 0.43018214432212887 -0.8983623348886722 -0.08881687880007882; 0.7899641342195538 0.32699590703939707 0.5186813505672173])
```

```julia
euler^3
```

```
Scattering.Rotation.RotationMatrix{Float64}([-0.20711300761088602 0.7472703153125533 0.6314200487243415; -0.6322711178708509 -0.5947556020638506 0.4964866637886771; 0.7465503570320742 -0.29639981387703873 0.5956590591512387])
```

```julia
euler^4
```

```
Scattering.Rotation.RotationMatrix{Float64}([0.7364715816744584 0.6696830270043788 0.09557328459445946; -0.644577211376976 0.651844177986726 0.3995239494677259; 0.2052555187063243 -0.35584239624735736 0.9117271308201462])
```

```julia
@test pow(euler, 100).R ≈ (euler^100).R
```

```
Test Passed
```

Benchmarks

```julia
using BenchmarkTools

@btime pow1($euler, 1000)
```

```
142.561 μs (3004 allocations: 172.31 KiB)
Scattering.Rotation.RotationMatrix{Float64}([-0.17617351956438138 0.7712758102440354 0.6116342988556001; -0.6592241548072412 -0.553880454852226 0.50856656934094; 0.7310173764848875 -0.31360814126062625 0.606022713280731])
```

The implementation of pow (or Scattering.^ which is the same as pow here)
is significantly faster than the naive implementation.

```julia
@btime $euler^1000
```

```
2.327 μs (49 allocations: 3.02 KiB)
Scattering.Rotation.RotationMatrix{Float64}([-0.1761735195643819 0.7712758102440348 0.6116342988555798; -0.6592241548072477 -0.5538804548522176 0.5085665693409378; 0.7310173764848691 -0.3136081412606315 0.6060227132807026])
```

### Testing applying AbstractRotation instance to a vector

Test multiplication of a `RotationMatrix` instance and a `Vector`

```julia
M = RotationMatrix(Rp)
v = [1.0, 2.0, 3.0]
@test M*v ≈ M.R * v
```

```
Test Passed
```

Test multiplication of a `RotationMatrix` instance and a `RVector` (`SVector`, `QVector`)

```julia
M = RotationMatrix(Rp)
r = RVector([1.0, 2.0, 3.0])
@test M*r ≈ M.R * r
```

```
Test Passed
```

Test multiplication of a `EulerAxisAngle` instance and a `Vector`

```julia
M = RotationMatrix(Rp)
Ma = EulerAxisAngle(M)
v = [1.0, 2.0, 3.0]
@test Ma*v ≈ M.R * v
```

```
Test Passed
```

Test multiplication of a `EulerAxisAngle` instance and a `RVector` (`SVector`, `QVector`)

```julia
M = RotationMatrix(Rp)
Ma = EulerAxisAngle(M)
v = RVector([1.0, 2.0, 3.0])
@test Ma*v ≈ M.R * v
```

```
Test Passed
```

Test multiplication of a `EulerAngle` instance and a `Vector`

```julia
M = RotationMatrix(Rp)
Ma = EulerAngle(M)
v = [1.0, 2.0, 3.0]
@test Ma*v ≈ M.R * v
```

```
Test Passed
```

Test multiplication of a `EulerAngle` instance and a `RVector` (`SVector`, `QVector`)

```julia
M = RotationMatrix(Rp)
Ma = EulerAngle(M)
v = RVector([1.0, 2.0, 3.0])
@test Ma*v ≈ M.R * v
```

```
Test Passed
```

## Acknowledgements

This work is partially supported by the General Program of the National Natural Science Foundation of China (No. 21873021).