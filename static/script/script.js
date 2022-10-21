const buttons = document.querySelectorAll('[data-slug]');

buttons.forEach(button => {
  button.addEventListener('click', (event) => {
    announcement = document.getElementById('posts');
    
    announcement.innerHTML = `
    <div class="col-md-4 card mb-4 mt-3">
      <div class="card-body">
        <div class="card-text">
          <div class="alert alert-primary" role="alert">
            <h4 class="alert-heading">Sorry to announce, but...</h4>
            <p>You must login to view comments/ add posts or 'like'</p>
                <a href="">
                  Back to posts
                </a><br>
                <a href="/accounts/login/" >
                  Log in
                </a>
          </div>
        </div>
      </div>
    </div>  
  `
  announcement.style.display = "flex"
  announcement.style.justifyContent = "center"
})
})


let theta = Math.PI / 4.0;
let new_theta = 0.0;
let new_x = 0.0;
let new_y = 0.0;
let wheel_radius = 200.00;
const photos = document.querySelectorAll('.photo');
const center = {
    x: parseFloat(getComputedStyle(photos[0]).left),
    y: parseFloat(getComputedStyle(photos[0]).top),

}

photos.forEach((photo, index) => {
    new_theta = theta * index;
    new_x = (Math.cos(new_theta) * wheel_radius);
    new_y = (-1.0 * Math.sin(new_theta) * wheel_radius);
    photo.style.left = `${center.x + new_x}px`;
    photo.style.top = `${center.y + new_y}px`;
});
