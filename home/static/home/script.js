document.getElementById("shuffle-button").addEventListener("click", function() {

    const currentQuote = document.querySelector("[data-quote-id]");
    const currentQuoteId = currentQuote ? currentQuote.dataset.quoteId : "";

    fetch("/shuffle-quote/?current=" + currentQuoteId)
        .then(response => response.text())
        .then(html => {
            document.getElementById("quote-container").innerHTML = html;
        });

});