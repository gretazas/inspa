// app.listen(process.env.PORT || 3000, function(){
//     console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
// });


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
            <p>You must login to view comments</p>
                <a href="/posts">
                  Back to posts
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

const healthbuttons = document.querySelectorAll('[healthdata-slug]');

healthbuttons.forEach(button => {
  button.addEventListener('click', (event) => {
    healthannouncement = document.getElementById('healthposts');
    
    healthannouncement.innerHTML = `
    <div class="col-md-4 card mb-4 mt-3">
      <div class="card-body">
        <div class="card-text">
          <div class="alert alert-primary" role="alert">
            <h4 class="alert-heading">Sorry to announce, but...</h4>
            <p>You must login to view comments</p>
                <a href="/posts">
                  Back to posts
                </a>
          </div>
        </div>
      </div>
    </div>  
  `
  healthannouncement.style.display = "flex"
  healthannouncement.style.justifyContent = "center"
})
})