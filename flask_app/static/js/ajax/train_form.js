var red, green, blue;

const changeColor = () => {
  red = Math.floor(Math.random()*256);
  green = Math.floor(Math.random()*256);
  blue = Math.floor(Math.random()*256);
  $("#main").prop('style',`background-color:rgb(${red},${green},${blue});`);
  $("#mood_select option:selected").prop('selected',false);
  $("#default_option").prop('selected',true);
}

$(document).ready(()=>{
  changeColor();
  $('#trainform').submit((e)=>{
    e.preventDefault();
    $("#submit").prop('disabled',true)
    const data = {"mood":$("#mood_select option:selected").val(),
                  "red":red,
                  "green":green,
                  "blue":blue
                  }
    $.ajax({
      method:'POST',
      url:`/train`,
      data:data,
    }).done((results)=>{
      if (results == "True"){
        $("#train_message").html("");
        changeColor();
      }else{
        $("#train_message").html("Please Select a Mood");
      }
      $("#submit").prop('disabled',false);
    });
  });
});