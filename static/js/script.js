document.getElementById('menu-btn').onclick = function() {
    document.querySelector('.navbar').classList.toggle('active');
}



// typing animation start
const fullText = "Turn your trash into cash—recycle and earn while helping the planet!"; // Text to type
    let index = 0;
    let typing = true;
    const typingSpeed = 100;
    const deletingSpeed = 50;
    const pauseDuration = 1000;

    function typeAndDelete() {
        const typewriterElement = document.getElementById("typewriter");

        if (typing) {
            // Typing the text
            if (index < fullText.length) {
                typewriterElement.textContent += fullText.charAt(index);
                index++;
                setTimeout(typeAndDelete, typingSpeed);
            } else {
                // Once typing is complete, pause and then start deleting
                typing = false;
                setTimeout(typeAndDelete, pauseDuration);
            }
        } else {
            // Deleting the text
            if (index > 0) {
                typewriterElement.textContent = fullText.substring(0, index - 1);
                index--;
                setTimeout(typeAndDelete, deletingSpeed);
            } else {
                // Once deleting is complete, pause and then start typing again
                typing = true;
                setTimeout(typeAndDelete, pauseDuration);
            }
        }
    }

    // Start the typing and deleting loop
    window.onload = typeAndDelete;
// typing animation end






// code for user face start
// Selecting the user icon and the sidebar
const userIcon = document.getElementById('user');
const sidebar = document.getElementById('sidebar');

// Toggle sidebar when the user icon is clicked





