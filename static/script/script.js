// app.listen(process.env.PORT || 3000, function(){
//     console.log("Express server listening on port %d in %s mode", this.address().port, app.settings.env);
// });


const button = document.getElementById('announcement');
button.addEventListener('click', (event) => {
    announcement = document.getElementById('announcement');
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
   
})