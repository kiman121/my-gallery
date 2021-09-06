$(document).ready(function () {
  $(document).on("click", ".view-photo-detail", function (e) {
    e.preventDefault();
    var photo_id = $(this).data("photoid");

    $.ajax({
      url: "/ajax/photo-detail/" + photo_id,
      dataType: "json",
      success: function (data) {
        var image_url = data.image_url,
          name = data.name,
          category = data.category,
          location = data.location,
          description = data.description,
          body =
            '<div class="card shadow-sm"><img class="bd-placeholder-img card-img-top" width="100%" src="' +
            image_url +
            '" alt="" /> <div class="card-body"><p class="card-text"><span>Name: </span>'+name+'</p><p class="card-text"><span>Category: </span>'+category+'</p><p class="card-text"><span>Location: </span>'+location+'</p><p class="card-text"><span>Description: </span>'+description+'</p></div> </div>';

        $("#photo_detail .modal-body").empty().append(body);

        $("#photo_detail").modal("show");
      }
    });
  });
  $(".image-tile").hover(
    function () {
      $(this)
        .find(".image-overlay")
        .empty()
        .html('<div class="text">x</div>');
      $(this).find(".image-overlay").show();
    },
    function () {
      $(".image-overlay").hide();
    }
  );
  $(".image-tile").hover(
    function () {
      // $(this).find('.image-copy').empty().append('<i class="fa fa-copy"></i>')
      $(this).find(".image-copy").show();
    },
    function () {
      $(".image-copy").hide();
    }
  );

  $(document).on("click",".image-copy", function(e){
    e.preventDefault()
    
    var image_url =  $(this).parents(".image-tile").find("img").attr("src");
    navigator.clipboard.writeText(image_url)
    
    navigator.clipboard.readText().then(url=>{
      console.log(`copied${url}`)
      $(this).empty().html('copied!');

      setTimeout(() => {
        $(this).empty().append('<i class="fa fa-copy"></i>')
      }, 2000);
    })
  
  });
});
