/**
 * Citation formatting and clipboard copy for publications page.
 *
 * Copies RICH TEXT (HTML) so that italic/bold formatting is preserved
 * when pasting into Word, Google Docs, etc.
 *
 * Supports three styles:
 *   ACS - American Chemical Society (e.g. Macromolecules, JACS)
 *   AIP - American Institute of Physics (e.g. J. Chem. Phys.)
 *   APS - American Physical Society (e.g. Phys. Rev. Lett.)
 */

/* ---- helpers ---- */

function parsePubData(li) {
    return {
        title: li.dataset.title || '',
        authors: li.dataset.authors || '',
        journal: li.dataset.journal || '',
        journalFull: li.dataset.journalFull || '',
        year: li.dataset.year || '',
        volume: li.dataset.volume || '',
        issue: li.dataset.issue || '',
        page: li.dataset.page || '',
        doi: li.dataset.doi || ''
    };
}

function splitAuthors(str) {
    return str.split(';')
        .map(function (s) { return s.trim(); })
        .filter(Boolean)
        .map(function (a) {
            var parts = a.split(',').map(function (s) { return s.trim(); });
            return { family: parts[0] || '', initials: parts[1] || '' };
        });
}

/* ---- formatters (return {html, plain}) ---- */

/**
 * ACS style (American Chemical Society)
 * Authors. Title. _J. Abbrev._ **Year**, _Vol_, Pages. DOI: xx
 */
function formatACS(d) {
    var authors = splitAuthors(d.authors);
    var authorStr = authors.map(function (a) { return a.family + ', ' + a.initials; }).join('; ');
    // Remove trailing period from last initial to avoid double periods
    if (authorStr.charAt(authorStr.length - 1) === '.') {
        authorStr = authorStr.slice(0, -1);
    }

    var plain = authorStr + '. ' + d.title + '. ' + d.journal;
    if (d.year) plain += ' ' + d.year + ',';
    if (d.volume) plain += ' ' + d.volume + ',';
    if (d.page) plain += ' ' + d.page;
    plain += '.';
    if (d.doi) plain += ' DOI: ' + d.doi;

    var html = authorStr + '. ' + d.title + '. <i>' + d.journal + '</i>';
    if (d.year) html += ' <b>' + d.year + '</b>,';
    if (d.volume) html += ' <i>' + d.volume + '</i>,';
    if (d.page) html += ' ' + d.page;
    html += '.';
    if (d.doi) html += ' DOI: ' + d.doi;

    return { html: html, plain: plain };
}

/**
 * AIP style (American Institute of Physics)
 * Authors, "Title," _J. Abbrev._ **Vol**, Pages (**Year**).
 */
function formatAIP(d) {
    var authors = splitAuthors(d.authors);
    var authorStr = authors.map(function (a) { return a.initials + ' ' + a.family; }).join(', ');

    var plain = authorStr + ', \u201c' + d.title + ',\u201d ' + d.journal;
    if (d.volume) plain += ' ' + d.volume;
    if (d.page) plain += ', ' + d.page;
    if (d.year) plain += ' (' + d.year + ')';
    plain += '.';

    var html = authorStr + ', \u201c' + d.title + ',\u201d <i>' + d.journal + '</i>';
    if (d.volume) html += ' <b>' + d.volume + '</b>';
    if (d.page) html += ', ' + d.page;
    if (d.year) html += ' (<b>' + d.year + '</b>)';
    html += '.';

    return { html: html, plain: plain };
}

/**
 * APS style (American Physical Society)
 * Authors, Title, _J. Abbrev._ **Vol**, Pages (**Year**).
 */
function formatAPS(d) {
    var authors = splitAuthors(d.authors);
    var authorStr;
    if (authors.length === 1) {
        authorStr = authors[0].initials + ' ' + authors[0].family;
    } else if (authors.length === 2) {
        authorStr = authors[0].initials + ' ' + authors[0].family + ' and ' +
            authors[1].initials + ' ' + authors[1].family;
    } else {
        var leading = authors.slice(0, -1).map(function (a) { return a.initials + ' ' + a.family; });
        var last = authors[authors.length - 1];
        authorStr = leading.join(', ') + ', and ' + last.initials + ' ' + last.family;
    }

    var plain = authorStr + ', ' + d.title + ', ' + d.journal;
    if (d.volume) plain += ' ' + d.volume;
    if (d.page) plain += ', ' + d.page;
    if (d.year) plain += ' (' + d.year + ')';
    plain += '.';

    var html = authorStr + ', ' + d.title + ', <i>' + d.journal + '</i>';
    if (d.volume) html += ' <b>' + d.volume + '</b>';
    if (d.page) html += ', ' + d.page;
    if (d.year) html += ' (<b>' + d.year + '</b>)';
    html += '.';

    return { html: html, plain: plain };
}

/* ---- UI ---- */

function toggleCiteMenu(btn) {
    var menu = btn.nextElementSibling;
    var isOpen = menu.classList.contains('open');
    document.querySelectorAll('.cite-menu.open').forEach(function (m) { m.classList.remove('open'); });
    if (!isOpen) menu.classList.add('open');
}

function copyCitation(menuBtn, style) {
    var li = menuBtn.closest('.pub-item');
    var d = parsePubData(li);
    var result;
    switch (style) {
        case 'acs': result = formatACS(d); break;
        case 'aip': result = formatAIP(d); break;
        case 'aps': result = formatAPS(d); break;
        default: result = formatACS(d);
    }
    menuBtn.closest('.cite-menu').classList.remove('open');
    copyRichText(result.html, result.plain);
}

/**
 * Copy both HTML (rich text) and plain text to clipboard.
 * Word/Docs will use the HTML version; plain editors get the text version.
 */
function copyRichText(html, plain) {
    if (navigator.clipboard && typeof ClipboardItem !== 'undefined') {
        try {
            var htmlBlob = new Blob([html], { type: 'text/html' });
            var textBlob = new Blob([plain], { type: 'text/plain' });
            var item = new ClipboardItem({
                'text/html': htmlBlob,
                'text/plain': textBlob
            });
            navigator.clipboard.write([item]).then(function () {
                showCiteToast('Citation copied!');
            }).catch(function () {
                fallbackRichCopy(html, plain);
            });
        } catch (e) {
            fallbackRichCopy(html, plain);
        }
    } else {
        fallbackRichCopy(html, plain);
    }
}

/**
 * Fallback: intercept the copy event and set clipboard data directly.
 * This avoids the contentEditable approach which converts spaces
 * to &nbsp; (showing as · in Word).
 */
function fallbackRichCopy(html, plain) {
    function onCopy(e) {
        e.clipboardData.setData('text/html', html);
        e.clipboardData.setData('text/plain', plain);
        e.preventDefault();
        document.removeEventListener('copy', onCopy, true);
    }
    document.addEventListener('copy', onCopy, true);
    // Need a selection for execCommand('copy') to fire the event
    var span = document.createElement('span');
    span.textContent = '\u200B'; // zero-width space
    span.style.position = 'fixed';
    span.style.left = '-9999px';
    document.body.appendChild(span);
    var range = document.createRange();
    range.selectNodeContents(span);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    try {
        document.execCommand('copy');
        showCiteToast('Citation copied!');
    } catch (e) {
        showCiteToast('Copy failed \u2013 please copy manually');
    }
    sel.removeAllRanges();
    document.body.removeChild(span);
    // cleanup in case handler didn't fire
    document.removeEventListener('copy', onCopy, true);
}

function showCiteToast(msg) {
    var existing = document.querySelector('.cite-toast');
    if (existing) existing.remove();
    var toast = document.createElement('div');
    toast.className = 'cite-toast';
    toast.textContent = msg;
    document.body.appendChild(toast);
    setTimeout(function () { toast.classList.add('show'); }, 10);
    setTimeout(function () {
        toast.classList.remove('show');
        setTimeout(function () { toast.remove(); }, 300);
    }, 2000);
}

document.addEventListener('click', function (e) {
    if (!e.target.closest('.cite-wrapper')) {
        document.querySelectorAll('.cite-menu.open').forEach(function (m) { m.classList.remove('open'); });
    }
});
