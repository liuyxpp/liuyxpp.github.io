---
layout: post
title: Polyorder Configuration File
description: A brief introduction to the format of the configuration file for Polyorder. Polyorder is a C++ software for computing complex self-assemble structures of block copolymers using self-consistent field theory (SCFT) methods.
author: lyx
date: 2015-04-06
modified: 2015-04-06
image:
    feature: false
categories: [Software]
tags: [Polyorder, Tutorial]
show_meta:
    info: true
---

The configuration file for [Polyorder] can be either in INI or in YAML format. Sample configuration files can be found in the `example` folder in the Polyorder project.

<!--more-->

## Format
-----

Here we use the YAML format to demonstrate how to write a configuration file for ``Polyorder``.

{% highlight yaml linenos %}
# Configurations for PolyOrder
---  # begin of new document
Version:  # corresponds to [section] in INI format
    # Format: <major>.<minor>, mapping to a float number.
    # Requires:
    #       <minor> = [0, 1, 2, ..., 9]
    # Compare versions, larger one is the latest one.
    # For example:
    #       9.2 > 9.1 > 8.0 > 7.9
    # certain Model may require minimum version number
    version     : 11.0
    format      : YAML  # the format of this configuration file
IO:  # I/O settings
    base_dir        : ./  # path should end with "/"
    data_file       : scft_out  # prefix of an output data file
    param_file      : param_out  # prefix of an output parameter file
    q_file          : q_out  # prefix of an output propagator data
    is_display      : true  # whether to display information
    is_save_data    : true  # whether to save data files
    is_save_q       : false  # whether to save propagator data
    # interval in unit of SCFT cycle for display
    display_interval: 100
    # interval in unit of SCFT cycle for recording data
    record_interval : 10
    # interval in unit of SCFT cycle for saving files
    # Use small interval to monitor intermediate results
    # Use large interval to avoid saving any intermediate results
    save_interval   : 20000
Model:  # SCFT model description
    # SCFT models, currently implemented are
    #       [AB, AB3+A]
    model           : AB
    # number of chain types
    # Example:
    #       AB + BC + C + M
    #       n_chains = 4
    n_chain         : 1
    # A list contains number of blocks for each chain.
    # For homopolymer and small molecules, n_block = 1.
    # We refer blocks, homopolymers, and small molecules to components.
    # Then number of components, n_component, is the sum of this list.
    n_block         : [2]
    # A list of the physical segment length of each component.
    # Size of this list is n_component.
    # Taking AB + C + M as an example,
    # where AB is an A-B diblock copolymer),
    # C is a homopolymer,
    # M is a small molecules.
    # Then, the returning list is
    #       [bA, bB, bC, bM]
    a               : [1.0, 1.0]
    # A list of the relative length of each component.
    # Size of this list is n_component.
    # Note the meaning of f depends on the choice of base.
    # For example, for an AB + C system, the list of f is
    #       [0.2, 0.8, 0.6]
    # which may mean
    #       f_A = N_A / N_AB
    #       f_B = N_B / N_AB
    #       f_C = N_C / N_AB
    # where N_AB = N_A + N_B.
    # Or, equivalently, f may write as
    #      [0.125, 0.5, 0.375]
    # which means
    #      f_A = N_A / N_ABC
    #      f_B = N_B / N_ABC
    #      f_C = N_C / N_ABC
    # where N_ABC = N_A + N_B + N_C.
    # The list is optional when Algorithm_MDE.f_mode = fix-ds.
    f               : [0.5, 0.5]
    # A list of the volume fraction of each chain specie.
    # Size of this list is n_chain.
    # In canonical ensemble, it is the volume fraction $\phi$.
    # In grand canonical ensemble, it is the activity $z$.
    # For example, in canonical ensemble
    #       AB + C
    #       phi = [phi_AB, phi_C]
    # where phi_AB + phi_C = 1.0 for mass conservation.
    # In grand canonical ensemble
    #       phi = [z_{AB}, z_C]
    phi             : [1.0]
    # A list of (\chi N) of each pair of components.
    # For n components, there are at most
    #       n * (n-1) / 2
    # (\chi N)s, where n = n_component.
    # These (\chi N)s are listed in the following way,
    #       AB + C + M
    #       [chiN_AB, chiN_AC, chiN_AM, chiN_BC, chiN_BM, chiN_CM]
    # (\chi N) between same type of component can be denoted as 0.
    chiN            : [30]
    is_compressible : false  # compressibility, [true, false]
    # for polymer brush
    graft_density   :
    # for implicit solvent
    excluded_volume :
UnitCell:  # unit cell description
    # Crystal system type of the unit cell
    # Available choices are
    # 1D:
    #       [lam]
    # 2D:
    #       [square, rect, hex]
    # 3D:
    #       [oblique, hex, cubic, tegragonal, orthorhombic,
    #        trigonal, monoclinic, triclinic]
    # All inputs are case-insensitive.
    CrystalSystemType   : Lamellar
    # Length and angles of a unit cell.
    #       [a, b, c, alpha, beta, gamma]
    # b, c should not have value for 1D.
    # c should not have value for 2D.
    a                   : 4.0
    b                   :
    c                   :
    alpha               :
    beta                :
    gamma               :
    # For Python package gyroid use only.
    # Not implemented in PolyOrder::Config.
    SymmetryGroup       :
    N_list              : []
    c_list              : []
Grid:  # numerical grid description
    # Grid dimension. Choose one of
    #       [1, 2, 3]
    dimension               : 1
    # Discrete points along each dimension
    #       [Lx, Ly, Lz]
    # For dimension = 1, Ly and Lz must be 1
    # For dimension = 2, Lz must be 1
    Lx                      : 64
    Ly                      : 1
    Lz                      : 1
    # Confinement settings
    # Confinement geometry. Choose one of
    #       [None, line, slit, slab, cube, disk, cylinder, sphere]
    # Currently, only [None, line, slit, slab] are implemented.
    # All inputs are case-insensitive.
    confine_geometry        : None
    # Grid type along each dimension. Choose one of
    #       [regular, chebyshev]
    # All inputs are case-insensitive.
    # For dimension = 1, grid_type_y and grid_type_z is optional.
    # For dimension = 2, grid_type_z is optional.
    grid_type_x             : Regular
    grid_type_y             :
    grid_type_z             :
    # A three-element vector describes the boundary condition:
    #       alpha * du/dx + beta * u = gamma
    # the vector is
    #       [alpha, beta, gamma]
    # See the definition of DBC, NBC, RBC, and PBC in cheb++ package.
    BC_coefficients_left    : []
    BC_coefficients_right   : []
    # Grid initialization
    # Way to initialize SCFT. Choose one of
    #       [field, density, propagator]
    # All inputs are case-insensitive.
    scft_init_type          : field
    # Way to initialize the numerical grid. Choose one of
    #       [random, file, constant]
    # All inputs are case-insensitive.
    gridInitType            : file
    # If gridInitType is random, then this option gives the random seed.
    # If random_seed is 0 or empty, then random seed is automatically
    # generated from current machine state.
    random_seed             :
    # If gridInitType is file, then this option gives the name of the
    # data file.
    field_data              : field_in_64.mat
Algorithm_MDE:  # description of the algorithm for solving MDE.
    # Algorithms, currently implemented are
    #       [OS, RQM4, ETDRK4]
    # All inputs are case-insensitive.
    algorithm       : RQM4
    # Mode for specifying the volume fraction of each component.
    # Choose one of
    #       [fix-ds, fix-Ms]
    # All options are case-insensitive.
    # Mode: fix-ds
    #       f = ds * (Ms-1)
    # Both ds and Ms should be provided.
    # Mode: fix-Ms
    #       ds = f / (Ms-1)
    # Both f and Ms should be provided.
    f_mode          : fix-Ms
    # A list of the size of contour step for each component.
    # Size of this list is n_component.
    # For small molecules, ds = 1.0
    # Example:
    #       AB + C + M
    #       [ds_A, ds_B, ds_C, 1.0]
    # It is optional when f_mode = fix-Ms
    ds              : [0.01, 0.01]
    # A list of the number of discrete contour points for each component.
    # Size of this list is n_component.
    # For small molecules, Ms = 1.
    # Example:
    #       AB + C + M
    #       [Ms_A, Ms_B, Ms_C, 1]
    Ms              : [51, 51]
    # Schemes for the ETDRK4 method. Choose one of
    #       [Cox-Matthews, Krogstad]
    # All options are case-insensitive.
    etdrk4_scheme   : Cox-Matthews
    # Number of discrete points along contour
    # for ETDRK4 coefficients compuation.
    # Can be left as empty, then the default value will be used.
    etdrk4_M        :
Algorithm_SCFT:  # Description of the SCFT algorithm
    # Algorithms. Choose one of
    #       [EM, Anderson, SIS, ETD]
    # Consult specific Model builder for the availability
    # of these algorithms.
    algorithm           : Anderson
    # A list of relaxation parameters.
    # Size of this list is (n_component + 1).
    # For incompressible model, the last element is the relaxation
    # coefficeint for incompressible field.
    # For compressible model, the last element is the
    # compressibility parameter.
    #lam                 : [0.05, 0.05, 5.0]  # for EM/ETDRK4
    lam                 : [0.9, 0.9, 5.0]  # for Anderson
    # Minimum number of SCFT cycles.
    min_iter            : 10
    # Maximum number of SCFT cycles.
    max_iter            : 500
    # Stop criteria.
    # The difference of H between neighboring SCFT cycles.
    thresh_H            : 1.0e-6
    # The residual error.
    thresh_residual     : 1.0e-8
    # The actual incompressiblity.
    thresh_incomp       :
    # Number of history for Anderson mixing algorithm.
    n_Anderson_mixing   : 10
Algorithm_Cell_Optimization:  # Description of cell size optimization algo
    # Choose one of
    #       [single, Brent]
    # All options are case-insensitive.
    algorithm       : Brent
    # Tolerance of the cell size of diffrence for Bent optimizaiton algo.
    tol_cell        : 1.0e-3
    # Maximum number of iterations allowed for Brent optimization algo.
    max_iter_cell   : 30
    # Cell size vector
    #       [a, b, c]
    # For Brent optimization, this is the initial cell size.
    batch_cell_min  : [4.0, 0.0, 0.0]
    # For Brent optimization, this is the search step size.
    batch_cell_step : [1.0, 0.0, 0.0]
    # For Brent optimization, this is not used.
    batch_cell_max  : []
Algorithm_Contour_Integration:  # Description of contour integration algo.
    # Choose one of
    #       [trapz, simpson]
    # All options are case-insensitive.
    algorithm       : Simpson
{% endhighlight %}

## Notes
-----

### All Format

- No difference will be caused by changing the suquences of the parameters.
- `BC_coefficients_left` and `BC_coefficients_right` vectors are $$(a,b,c)$$ where $$au_x + bu = c$$.
- The minimum `tol_cell` is 3.0e-8.

### INI Only

- Comments can be added as a "#"-leading-line.
- Key and value should be comparted by a equal sign, and all blank character
  between keys and values will be neglected automatically.
- The trailing whitespaces may cause serious problem, they should be removed carefully.
- Support section name. Section name is enclosed by square bracket.

### YAML Only

- For YAML format, block comments are lead by "#", and inline comments are also lead by "#" but should have at least one space between "#" and main content.

## Changelog
-----

### Version 11.0

- Now configuration file is in YAML format.

Version 10.3

- Add `Model.phi` to specify the volume fraction of each specie.

Version 10.2

- Add `Grid.scft_init_type` to specify initialization densities or potential fields or propagators.

Version 10.1

- Add `Algorithm_MDE.f_mode` to allow controlling how to determine volume fraction.

Version 10.0

- Add `Version`, `Algorithm_MDE`, `Algorithm_SCFT`, `Algorithm_Cell_Optimization`, `Algorithm_Contour_Integration` sections.
- Remove `SCFT.is_batch_cell`
- Move some keys to new sections
- Break SCFT section into `IO` and `Algorithm_SCFT` sections.
- Use `tests/test_config_v10` to test whether a configuration file is consistent internally.

Version 9.0 and before

- 2014.06.12 Compatible with current version of Polyorder.
- 2013.07.31 Compatible with scftpy/bulk.
- 2013.06.24 Add `q_file`.
- 2012.11.08 Add `BC` support.
- 2012.10.11 Currently, only supports one type of chain.
- 2012.10.10 Break compatability with previous version. Only for scftpy use. Move `Ms` from `Model` section to `Grid` section.
- 2012.4.24 Add `dielectric_constant`, `charge_distribution` to `Algorithm` section. Delete `isAnnealed` from `Model` section.
- 2012.4.22 Add `Algorithm` section
- 2012.4.20 Add `fft2mg_mode` and `fft2mg_interp`
- 2012.4.18 Add `gensym.py` support

## ToDo List
-----

- Refractor `Config.cc/Config.h` to let `Config` be a format independent class. Support both INI and YAML format. And easy to support other formats, such as JSON, XML, etc.

## Reference
-----

- [Polyorder][polyorder]

[polyorder]: {{ site.url }}/software/
