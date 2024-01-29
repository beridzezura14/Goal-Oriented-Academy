const subscribe = document.getElementById('subscribe');
const contentRow = document.getElementById('content-row');
const sent = document.getElementById('sent');
const text = document.getElementById('text')

subscribe.addEventListener('click', function(e){
    const inputText = document.getElementById('text');
    const inputValue = inputText.value;

    e.preventDefault(); // ამან გვიშველა

    if(inputValue.includes('@') && inputValue.includes('.')){
      sent.style.display = 'block';
      contentRow.style.display = 'none';


      console.log('mgeli datvi') // და ჩვენ დათოიემ
    }else {
      // Set the text content and apply the "invalid" class
      document.getElementById('output').textContent = 'valid email requared.';
      document.getElementById('output').className = 'invalid';
      text.style.border = '1px solid red'
      text.style.backgroundColor = '#ff000022'
            // Apply the "invalid" class to the input field
      inputText.className = 'invalid';
    }
})
