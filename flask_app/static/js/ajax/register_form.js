const validators = {'username':false,'email':false,'password':false,'confirm_password':false}
$(document).ready(()=>{
    $('#submit').prop('disabled',true);
    Object.keys(validators).forEach(validator => {
        $(`#${validator}`).keyup(()=>{checkValid(validator)});
        $(`#${validator}`).focusout(()=>{checkAllValid(validator)});
    });
});

const checkAllValid = () => {
  Object.keys(validators).forEach(validator => {
    checkValid(validator)
  })
}
const checkValid = (id) => {
    var data = $("#regform").serialize()
    $.ajax({
            method:'POST',
            url:`/ajax/user/${id}`,
            data:data
    })
    .done((results) => {
        if(results.length < 3){
            $(`#${id}`).removeClass('is-invalid');
            validators[id]=true;
        }
        else{
            $(`#${id}`).addClass('is-invalid');
            validators[id]=false;
        }
        $(`#${id}_message`).html(results);
        if(Object.values(validators).every(validator => validator === true)){
            $('#submit').prop('disabled',false);
        }else{
            $('#submit').prop('disabled',true);
        }
    });
}