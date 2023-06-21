document.addEventListener('DOMContentLoaded', function() {

    // whenever the site gets clicked
    document.body.addEventListener('click', event => {
        
        const clicked_element = event.target;

        // --- load email page
        const like_buttons   = document.querySelectorAll(".like-button")
        like_buttons.forEach( (like_button) => {
        if (like_button.contains(clicked_element)) {
            toggle_like(like_button.dataset.id)
        }
        });
    });


    function toggle_like(post_id) {
        fetch('/like_deslike_post/' + post_id)
        .then(response => response.json())
        .then(message => {
            // ... do something else with email ...
            console.log(message)
        });
    }

});