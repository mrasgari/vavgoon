/*!
* Start Bootstrap - Modern Business v5.0.6 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

let inputTextArea = document.getElementById("input-textarea");
let wordCount = document.getElementById("word-count");
let charcCount = document.getElementById("charc-count");
inputTextArea.addEventListener("input", () => {
  charcCount.textContent = inputTextArea.value.length;
  let txt = inputTextArea.value.trim();
  wordCount.textContent = txt.split(/\s+/).filter((item) => item).length;
});
$('#submit-btn').click(function(){
  let text=$('#input-textarea').val();
  $.post("http://127.0.0.1:8000/api/v1/normalize/",
  {
    text: text,

  },
  function(data, status){
    $('#input-textarea').val(data)
  });
});
