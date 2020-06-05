function copy(){
  $("#copy_url").select()
  document.execCommand('copy')
  alert('Image link copied to clipboard')
}

function showModal(imgname,imgdesc,imgurl,imgcat,imgloc, imgcity, imgplc,copyurl){
  $("#imageModal").modal("show")
  $(".modal-title").text(imgname)
  $("#imgdescription").text(imgdesc)
  $(".mod-img").attr("src",imgurl)
  $(".imgcat").text('Category: '+imgcat)
  $(".imgloc").text('Country: ' + imgloc)
  $(".imgcity").text('City: ' + imgcity)
  $(".imgplc").text('Place: ' + imgplc)
  $("#copy_url").val(copyurl)
}


