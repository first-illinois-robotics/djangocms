const collapseElementList = [].slice.call(document.querySelectorAll('.overflow-program-header-target'));
collapseElementList.map(function (collapseEl: Element) {
    collapseEl.addEventListener('show.bs.collapse', function () {
        const indicator = document.getElementsByClassName(collapseEl.id + "-indicator").item(0);
        indicator.classList.add("rotated");
    });
    collapseEl.addEventListener('hide.bs.collapse', function () {
        const indicator = document.getElementsByClassName(collapseEl.id + "-indicator").item(0);
        indicator.classList.remove("rotated");
    })
});
