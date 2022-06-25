
main();

function main(){
    hideProgressBar("progress-summary-of-order")
    hideProgressBar("progress-payment-details")
}

function hideProgressBar(){
    const progress = document.getElementById(id);
    progress.style.visibilty="hidden";
}