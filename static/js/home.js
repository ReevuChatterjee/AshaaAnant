document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".count");

  counters.forEach(counter => {
    const animate = () => {
      const target = +counter.getAttribute("data-target");
      const count = +counter.innerText;
      const speed = 200; // Lower = faster

      const increment = target / speed;

      if (count < target) {
        counter.innerText = Math.ceil(count + increment);
        setTimeout(animate, 20);
      } else {
        counter.innerText = target.toLocaleString("en-IN");
      }
    };

    animate();
  });
});
