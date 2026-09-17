const CARS = [
  { name: "Tesla Model S Plaid", year: 2023, type: "ev",    km: "18,400 km", price: 84900, emoji: "⚡", tag: "Electric" },
  { name: "BMW M4 Competition",  year: 2022, type: "sedan", km: "31,200 km", price: 72500, emoji: "🏎️", tag: "Sedan" },
  { name: "Audi Q7 quattro",     year: 2023, type: "suv",   km: "22,900 km", price: 61300, emoji: "🚙", tag: "SUV" },
  { name: "Mercedes EQE 350+",   year: 2024, type: "ev",    km: "9,100 km",  price: 68900, emoji: "🔋", tag: "Electric" },
  { name: "Porsche Macan S",     year: 2022, type: "suv",   km: "37,500 km", price: 65400, emoji: "🚘", tag: "SUV" },
  { name: "Lexus IS 350 F Sport",year: 2023, type: "sedan", km: "14,700 km", price: 48200, emoji: "🚗", tag: "Sedan" },
];

const money = new Intl.NumberFormat("en-US", {
  style: "currency", currency: "USD", maximumFractionDigits: 0,
});

const grid = document.getElementById("carGrid");

function render(filter) {
  const list = filter === "all" ? CARS : CARS.filter((c) => c.type === filter);
  grid.innerHTML = list
    .map(
      (c) => `
      <article class="car">
        <div class="thumb" aria-hidden="true">${c.emoji}</div>
        <div class="body">
          <h3>${c.name}</h3>
          <p class="meta">${c.year} · ${c.km}</p>
          <div class="foot">
            <span class="price">${money.format(c.price)}</span>
            <span class="tag">${c.tag}</span>
          </div>
        </div>
      </article>`
    )
    .join("");
}

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    document.querySelectorAll(".chip").forEach((c) => c.classList.remove("is-active"));
    chip.classList.add("is-active");
    render(chip.dataset.filter);
  });
});

const form = document.getElementById("leadForm");
const msg = document.getElementById("formMsg");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = new FormData(form);
  const name = String(data.get("name") || "").trim();
  const email = String(data.get("email") || "").trim();

  if (!name || !email.includes("@")) {
    msg.textContent = "Please enter your name and a valid email address.";
    return;
  }
  msg.textContent = `Thanks ${name} — we'll email you at ${email} to confirm a slot.`;
  form.reset();
});

document.getElementById("year").textContent = new Date().getFullYear();
render("all");
