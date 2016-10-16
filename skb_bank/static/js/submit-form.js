/**
 * Created by Vuletic on 16.10.2016.
 */
$( document ).ready(function(){

    $('#form-submit').click(function () {

        var answers = {
            type: "",
            intention: "",
            age: "",
            income: "",
            urgency: "",
            insurance: "",
            citizenship: "",
            bank: "",
            interest: "",
            buy_insurance: ""
        }

        if($('#f-option').is(':checked')) { answers.type = "Loan" }
        if($('#s-option').is(':checked')) { answers.type = "Insurance" }
        if($('#t-option').is(':checked')) { answers.type = "Investment" }

        if($('#house-option').is(':checked')) { answers.intention = "house" }
        if($('#car-option').is(':checked')) { answers.intention = "car" }
        if($('#other-option').is(':checked')) { answers.intention = "other" }

        answers.age = $('#ageGroup').val();

        if($('#unemployed-option').is(':checked')) { answers.income = 0 }
        if($('#less-850-option').is(':checked')) { answers.income = 850 }
        if($('#between-850-1250-option').is(':checked')) { answers.income = 1250 }
        if($('#more-1250-option').is(':checked')) { answers.income = 1300 }

        if($('#not-urgent-option').is(':checked')) { answers.urgency = 5 }
        if($('#urgent-option').is(':checked')) { answers.urgency = 3 }
        if($('#very-urgent-option').is(':checked')) { answers.urgency = 1 }
        
        answers.insurance = $('#loanInsurance').val();

        if($('#slovenia-option').is(':checked')) { answers.citizenship = "Slo" }
        if($('#eu-option').is(':checked')) { answers.citizenship = "EU" }
        if($('#non-eu-option').is(':checked')) { answers.citizenship = "non-EU" }

        if($('#yes-client-skb-option').is(':checked')) { answers.bank = "SKB" }
        if($('#yes-client-no-skb-option').is(':checked')) { answers.bank = "other" }
        if($('#no-client-option').is(':checked')) { answers.bank = "no" }

        if($('#fixed-option').is(':checked')) { answers.interest = "Fixed" }
        if($('#variabled-option').is(':checked')) { answers.interest = "Variabled" }

        if($('#yes-better-option').is(':checked')) { answers.buy_insurance = true }
        if($('#no-better-option').is(':checked')) { answers.buy_insurance = false }

        console.log(answers);


        /*$.post( "ajax/test.html", function( data ) {
          $( ".result" ).html( data );
        });*/

    });


});