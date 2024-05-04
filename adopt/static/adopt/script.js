document.addEventListener('DOMContentLoaded', function() {

    const more_btns = document.querySelectorAll('.more');
    more_btns.forEach(link => {
        link.addEventListener('click', more);
    });

    const like_btns = document.querySelectorAll('.btn.like');
    like_btns.forEach(button => {
        button.addEventListener('click', like);
    });

    const card_images = document.querySelectorAll('.card-img-container');
    card_images.forEach( div => {
        //let pet_id = div.dataset.pet; 
        div.addEventListener('click', detail);
    }); 
});


function detail() {
    
    let pet_id = this.dataset.pet;
    let url = '/detail/' + pet_id;
    location.href = url;

}


function like(event) {
    event.preventDefault();

    // Submit post via POST method using Fetch()
    fetch('/like', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            pet_id: this.dataset.pet
        })
    }) 
    .then(response => response.json())
    .then(result => { 
        // Update Likes Count
        this.innerHTML = result.count;
        console.log("like count " + result.count);
    })
    .catch(error => { console.error('Only authenticated user is allowed to like'), error}); 
}

function more(event) {

    let pet_id = this.dataset.pet;
    let desc_id = "desc" + pet_id;

    let text =  document.getElementById(desc_id);
    console.log("he");
    if (text.className == 'card-text initial') {
        text.className = 'card-text full';
        event.target.innerHTML = 'See less';
    } else {
        text.className = 'card-text initial';
        event.target.innerHTML = 'See More';
    }
}