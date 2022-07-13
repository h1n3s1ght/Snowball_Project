$(document).ready(function(){
    $('.card').click(function(){
        $('.showEach').toggle('slide');
    });
});



let TotalDebt = 0;
let MinMonPay = 0;

$(document).ready(function(){
      console.log("loaded")
      TotalDebt = 0;
      MinMonPay = 0;
      $('#getTotalValues').each(function(){
        TotalDebt += $(this).val() || 0;
        return TotalDebt;
      });
      $('#getMinValues').each(function(){
        MinMonPay += $(this).val() || 0;
        return MinMonPay;
      });
      console.log(TotalDebt);
      console.log(MinMonPay)
    });