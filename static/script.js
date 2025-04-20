document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const themeText = document.getElementById("theme-text");
  const themeIcon = document.querySelector(".theme-icon");
  const sidebarToggle = document.getElementById("sidebar-toggle");
  const sidebar = document.getElementById("sidebar");
  const categoryFilter = document.getElementById("category-filter");
  const categorySections = document.querySelectorAll(".category-section");
  const showAllLinks = document.querySelectorAll(".show-all");
  const searchInput = document.getElementById("text-search");
  const searchButton = document.getElementById("search-button");
  const allCards = document.querySelectorAll(".podcast-card");

  // THEME SETUP
  function setTheme(mode) {
    document.documentElement.setAttribute("data-theme", mode);
    localStorage.setItem("theme", mode);

    if (mode === "dark") {
      themeText.textContent = "Light Mode";
      themeIcon.classList.remove("fa-moon");
      themeIcon.classList.add("fa-sun");
    } else {
      themeText.textContent = "Dark Mode";
      themeIcon.classList.remove("fa-sun");
      themeIcon.classList.add("fa-moon");
    }
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute("data-theme");
    const newTheme = currentTheme === "dark" ? "light" : "dark";
    setTheme(newTheme);
  }

  // Load saved theme
  const savedTheme = localStorage.getItem("theme") || "dark";
  setTheme(savedTheme);

  themeToggle.addEventListener("click", (e) => {
    e.preventDefault();
    toggleTheme();
  });

  // SIDEBAR TOGGLE
  sidebarToggle?.addEventListener("click", () => {
    sidebar?.classList.toggle("show");
  });

  // CATEGORY + SEARCH FILTERS
  function filterByTitle() {
    const query = searchInput.value.trim().toLowerCase();
    const foundInCategories = new Set();

    if (query === "") {
      categorySections.forEach((section) => (section.style.display = "block"));
      allCards.forEach((card) => (card.style.display = "block"));
      return;
    }

    allCards.forEach((card) => {
      const title = card.getAttribute("data-title").toLowerCase();
      const matches = title.includes(query);

      card.style.display = matches ? "block" : "none";

      if (matches) {
        const parentSection = card.closest(".category-section");
        if (parentSection) foundInCategories.add(parentSection);
      }
    });

    categorySections.forEach((section) => {
      section.style.display = foundInCategories.has(section) ? "block" : "none";
    });

    categoryFilter.value = "all"; // Reset dropdown
  }

  categoryFilter.addEventListener("change", function () {
    const selected = this.value;
    searchInput.value = "";

    categorySections.forEach((section) => {
      const sectionCategory = section.getAttribute("data-category");
      section.style.display =
        selected === "all" || sectionCategory === selected ? "block" : "none";
    });

    allCards.forEach((card) => (card.style.display = "block"));
  });

  showAllLinks.forEach((link) => {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      const selectedCategory = this.getAttribute("data-category");

      categorySections.forEach((section) => {
        const category = section.getAttribute("data-category");
        section.style.display =
          category === selectedCategory ? "block" : "none";
      });

      categoryFilter.value = selectedCategory;
      searchInput.value = "";
      allCards.forEach((card) => (card.style.display = "block"));
    });
  });

  searchButton.addEventListener("click", filterByTitle);
  searchInput.addEventListener("input", filterByTitle);
});
