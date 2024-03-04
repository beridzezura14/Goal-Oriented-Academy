const menu = document.querySelector(".open-icon");
const closeMenu = document.querySelector(".close-icon");
const menuList = document.querySelector(".menu-list");

menu.addEventListener("click", function () {
  menu.classList.add("close-btn");
  closeMenu.classList.add("open-btn");
  menuList.classList.add("open-btn");
});
closeMenu.addEventListener("click", function () {
  menu.classList.remove("close-btn");
  closeMenu.classList.remove("open-btn");
  menuList.classList.remove("open-btn");
});
