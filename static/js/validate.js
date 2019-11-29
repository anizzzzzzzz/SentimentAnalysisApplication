function validateTextArea(){
    var review = document.getElementById('review').value;
    console.log(review);
    if(review.length < 10){
        document.getElementsByClassName('message')[0].innerHTML = "* It must contain more than 10 char.";
        return false;
    }
    return true;
}

function onPredictionReviewSubmit(predicted){
    let review_text = document.getElementById('result-textarea').value;
    let review_data = {text:review_text, prediction:predicted};

    $.ajax({
        type:'POST',
        url:'/save-review',
        data: JSON.stringify(review_data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        complete : function () {
            document.getElementById('correct_pred_btn').style.display = 'none';
            document.getElementById('incorrect_pred_btn').style.display = 'none';
            document.getElementById('next-review-submit').style.display = 'inline-block';
        }
    });
}

function submitAnotherReview() {
   window.location.href='/'
}