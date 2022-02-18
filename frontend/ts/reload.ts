// taken from https://github.com/django-cms/djangocms-template/blob/4b516fd32c575c6f303b506babe7d391e84cdaeb/frontend/vendor/index.js

declare var CMS: any;

import $ from "jquery";

export function initReloadScriptsOnContentRefresh() {
    const isCmsPresent = window.hasOwnProperty('CMS');
    if (isCmsPresent) {
        initScriptReloadListener();
    }
}


function initScriptReloadListener() {
    const cmsPageEditedEvent = 'cms-content-refresh';
    CMS.$(window).on(cmsPageEditedEvent, () => {
        $('script[data-is-reload-on-page-edit]').each((index, element) => {
            forceScriptReload.call(element);
        });
        window.document.dispatchEvent(new Event('DOMContentLoaded', {
            bubbles: true,
            cancelable: true,
        }));
    });
}


function forceScriptReload() {
    const isScriptHasSourceAttr = $(this).attr('src');
    if (isScriptHasSourceAttr) {
        const scriptSrc = $(this).attr('src') as string;
        $(this).remove();
        $('<script>').attr('src', scriptSrc).appendTo('head');
    } else {
        const scriptBody = $(this).html();
        const scriptParent = $(this).parent()
        $(this).remove();
        eval(
            $('<script/>', {html: scriptBody})
                .appendTo(scriptParent)
                .text()
        );
    }
}