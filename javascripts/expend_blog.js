console.log("expand_blog.js loaded");
document.addEventListener("DOMContentLoaded", function () {
  // 选中所有侧边栏折叠项的 input
  document.querySelectorAll('.md-nav__toggle').forEach(function(input) {
    if (!input.checked) input.checked = true;
  });
});