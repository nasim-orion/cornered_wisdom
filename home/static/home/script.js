document.getElementById("shuffle-button").addEventListener("click", function() {

    fetch("/shuffle-quote/")
        .then(response => response.text())
        .then(html => {
            document.getElementById("quote-container").innerHTML = html;
        });

});