let i = 0;


$(document).ready(function () {

    $('a[href="#java_paint"]').click(function () {
        $("#java_paint").fadeIn("slow");
    });
    $('a[href="#pyduino_pong"]').click(function () {
        $("#pyduino_pong").fadeIn("slow");
    });
});

/**
 * A function that calls the typingAnimation() method to after a certain period of time to induce a delay 
 * @param {[string]} id [The id located in a certain tag]
 * @param {[string]} text [the literal string value to implement the animation on]
 * @param {[int]} speed [The speed in which the animation will be run at]
 * @returns {} [void]
 */
function beginTypingAnimation(id, text, speed = 50) {
    setTimeout(function () {
        typingAnimation(id, text);
    }, speed);
}


/**
 * Creates a typing animation with the provided string value
 * @param {[string]} id [The id located in a certain tag]
 * @param {[string]} text [the literal string value to implement the animation on]
 * @param {[int]} speed [The speed in which the animation will be run at]
 * @returns {} [void]
 */
function typingAnimation(id, text, speed = 50) {
    var nameElement = document.getElementById(id);
    if (i < text.length) {
        if (text[i] === ' ') {
            nameElement.innerText += '\u00A0'; // If the current character is a white space, add it without timeout
        } else {
            nameElement.innerText += text.charAt(i); // Otherwise, proceed with the typing animation
        }

        i++;
        setTimeout(function () {
            typingAnimation(id, text);
        }, speed);

    }
}