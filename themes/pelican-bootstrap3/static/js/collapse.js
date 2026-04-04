document.addEventListener("DOMContentLoaded", function () {
  document.addEventListener("click", function (e) {
    var trigger = e.target.closest("[data-toggle='collapse']");
    if (!trigger) return;

    e.preventDefault();

    var targetSel =
      trigger.getAttribute("data-target") ||
      trigger.getAttribute("href");
    var target = document.querySelector(targetSel);
    if (!target) return;

    var parent = trigger.getAttribute("data-parent");
    if (parent) {
      var siblings = document.querySelectorAll(parent + " .in");
      for (var i = 0; i < siblings.length; i++) {
        if (siblings[i] !== target) {
          siblings[i].classList.remove("in");
        }
      }
    }

    target.classList.toggle("in");
  });
});
