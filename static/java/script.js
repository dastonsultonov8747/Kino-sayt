
function toggleDropdown() {
    var dropdown = document.querySelector('.dropdown');
    dropdown.classList.toggle('active');
}

// Modalni ochish funksiyasi
function openModal() {
    const modal = document.getElementById('video-modal');
    const video = document.getElementById('modal-video');
    modal.style.display = 'flex'; // Modalni ko'rsatish
    video.play();
}

// Modalni yopish funksiyasi
function closeModal() {
    const modal = document.getElementById('video-modal');
    const video = document.getElementById('modal-video');
    video.pause(); // Video pauza
    modal.style.display = 'none'; // Modalni yashirish
}

// Video boshqaruv funksiyalari
function togglePlayPause() {
    const video = document.getElementById('modal-video');
    if (video.paused) {
        video.play();
    } else {
        video.pause();
    }
}

function rewindVideo() {
    const video = document.getElementById('modal-video');
    video.currentTime -= 10; // 10 sekund orqaga
}

function forwardVideo() {
    const video = document.getElementById('modal-video');
    video.currentTime += 10; // 10 sekund oldinga
}

// Ovozni boshqarish funksiyasi
function toggleSound() {
    const video = document.getElementById('intro-video');
    const soundBtn = document.getElementById('sound-btn');
    if (video.muted) {
        video.muted = false;
        soundBtn.textContent = '🔊'; // Ovozni yoqish
    } else {
        video.muted = true;
        soundBtn.textContent = '🔇'; // Ovozni o'chirish
    }
}

// Play Now tugmasini bosganda videoni ochish
function playNow() {
    openModal();
}
