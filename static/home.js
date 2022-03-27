const indicator = document.querySelector('.nav-indicator');
const items = document.querySelectorAll('.nav-item');



function showModal(image_id,name,description,url,location,location_id,category,category_id,posted){
    $("#img-name").text(name)
    $("#imageModal").modal("show")
    $(".modal-title").text(name)
    var img_link ="/image/" + image_id
    $(".mod-img").attr("src",url)
    $("#img-link").attr("href", img_link)
    $("#img-desc").text(description)
    var location_link = "/location/" + location_id
    $("#img-loc").text(location)
    $("#img-loc").attr("href", location_link)
    var category_link = "/category/" + category_id
    $("#img-cat").attr("href", category_link)
    $("#img-cat").text("#" + category)
    $("#img-pos").text(posted)
    $("#copy-url").val(window.location.origin + "/image/" + image_id)
}

function share(){
    $("#copy-url").select()
    document.execCommand('copy');
    alert("Share link has been copied to your clipboard!")
}