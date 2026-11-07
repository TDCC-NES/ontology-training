// Keep the page contents in view instead of scrolling to the active chapter.
window.addEventListener("load", () => {
    const sidebar = document.getElementById("pst-primary-sidebar");
    if (sidebar) sidebar.scrollTop = 0;

    const pageContents = document.getElementById("pst-page-toc-nav");
    pageContents?.addEventListener("click", (event) => {
        if (!event.target.closest("a[href^='#']")) return;
        const drawer = document.getElementById("pst-primary-sidebar-modal");
        if (drawer?.open) drawer.close();
    });
});
