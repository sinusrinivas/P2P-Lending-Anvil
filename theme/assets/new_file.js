function openInvestNowForm() {
  anvil.server.call('open_invest_now_form')
    .then(function() {
        // Optional: Handle success, if needed
    })
    .catch(function(err) {
        // Optional: Handle error, if needed
        console.error("Error opening Invest Now form:", err);
    });
}
