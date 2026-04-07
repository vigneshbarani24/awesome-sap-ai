// ====== GSAP + ScrollTrigger Registration ======
gsap.registerPlugin(ScrollTrigger);

// ====== HERO ANIMATIONS ======
const heroTl = gsap.timeline({ defaults: { ease: "power3.out" } });

heroTl
  .from(".hero-badge", { opacity: 0, y: 20, duration: 0.6 })
  .from(".hero-title-line", { opacity: 0, y: 40, duration: 0.8, stagger: 0.15 }, "-=0.3")
  .from(".hero-subtitle", { opacity: 0, y: 20, duration: 0.6 }, "-=0.4")
  .from(".hero-cta .btn", { opacity: 0, y: 20, duration: 0.5, stagger: 0.1 }, "-=0.3")
  .from(".stat", { opacity: 0, y: 20, duration: 0.5, stagger: 0.1 }, "-=0.2")
  .from(".scroll-indicator", { opacity: 0, duration: 0.6 }, "-=0.2");

// ====== COUNTER ANIMATION ======
document.querySelectorAll(".stat-number").forEach(function (el) {
  var target = parseInt(el.getAttribute("data-count"), 10);
  gsap.to(el, {
    textContent: target,
    duration: 2,
    delay: 1,
    snap: { textContent: 1 },
    ease: "power2.out",
    onUpdate: function () {
      el.textContent = Math.round(parseFloat(el.textContent));
    },
  });
});

// ====== LEVEL ANIMATIONS (ScrollTrigger) ======
document.querySelectorAll(".level").forEach(function (level) {
  gsap.to(level, {
    opacity: 1,
    y: 0,
    duration: 0.8,
    ease: "power2.out",
    scrollTrigger: {
      trigger: level,
      start: "top 80%",
      end: "top 50%",
      toggleActions: "play none none none",
    },
  });

  // Stagger cards within each level
  var cards = level.querySelectorAll(".card");
  gsap.from(cards, {
    opacity: 0,
    y: 30,
    duration: 0.5,
    stagger: 0.1,
    ease: "power2.out",
    scrollTrigger: {
      trigger: level,
      start: "top 70%",
      toggleActions: "play none none none",
    },
  });
});

// ====== PROGRESS BAR ======
var progressFill = document.getElementById("progressFill");
var levels = document.querySelectorAll(".level");
var progressLabels = document.querySelectorAll(".progress-labels span");

ScrollTrigger.create({
  trigger: ".roadmap",
  start: "top top",
  end: "bottom bottom",
  onUpdate: function (self) {
    var progress = self.progress;
    progressFill.style.width = (progress * 100) + "%";

    // Highlight active progress label
    var activeIndex = Math.min(
      Math.floor(progress * progressLabels.length),
      progressLabels.length - 1
    );
    progressLabels.forEach(function (label, i) {
      if (i <= activeIndex) {
        label.classList.add("active");
      } else {
        label.classList.remove("active");
      }
    });
  },
});

// ====== PEOPLE CARDS ======
var personCards = document.querySelectorAll(".person-card");
gsap.to(personCards, {
  opacity: 1,
  y: 0,
  duration: 0.5,
  stagger: 0.08,
  ease: "power2.out",
  scrollTrigger: {
    trigger: ".people-section",
    start: "top 75%",
    toggleActions: "play none none none",
  },
});

// ====== SECTION TITLE ANIMATIONS ======
document.querySelectorAll(".section-title").forEach(function (title) {
  gsap.from(title, {
    opacity: 0,
    y: 30,
    duration: 0.7,
    ease: "power2.out",
    scrollTrigger: {
      trigger: title,
      start: "top 85%",
      toggleActions: "play none none none",
    },
  });
});

document.querySelectorAll(".section-subtitle").forEach(function (sub) {
  gsap.from(sub, {
    opacity: 0,
    y: 20,
    duration: 0.6,
    delay: 0.15,
    ease: "power2.out",
    scrollTrigger: {
      trigger: sub,
      start: "top 85%",
      toggleActions: "play none none none",
    },
  });
});

// ====== CTA SECTION ======
gsap.from(".cta-content", {
  opacity: 0,
  y: 40,
  duration: 0.8,
  ease: "power2.out",
  scrollTrigger: {
    trigger: ".cta-section",
    start: "top 75%",
    toggleActions: "play none none none",
  },
});

// ====== CARD HOVER TILT (subtle) ======
document.querySelectorAll(".card, .person-card").forEach(function (card) {
  card.addEventListener("mousemove", function (e) {
    var rect = card.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var y = e.clientY - rect.top;
    var centerX = rect.width / 2;
    var centerY = rect.height / 2;
    var rotateX = ((y - centerY) / centerY) * -3;
    var rotateY = ((x - centerX) / centerX) * 3;

    gsap.to(card, {
      rotateX: rotateX,
      rotateY: rotateY,
      duration: 0.3,
      ease: "power2.out",
      transformPerspective: 800,
    });
  });

  card.addEventListener("mouseleave", function () {
    gsap.to(card, {
      rotateX: 0,
      rotateY: 0,
      duration: 0.5,
      ease: "power2.out",
    });
  });
});
