function copy(){
  $("#input").select()
  document.execCommand('copy')
  alert('Image link copied to clipboard')
}

