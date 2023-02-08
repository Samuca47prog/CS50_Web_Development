document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // load email page
  document.body.addEventListener('click', event => {
    
    const clicked_element = event.target;

    const emails   = document.querySelectorAll(".email-box")
    emails.forEach( (email) => {
      if (email.contains(clicked_element)) {
        console.log(email);
      }
    });

  })


  //send email when form is submitted
  document.querySelector("#compose-form").onsubmit = function() {
    const recipients = document.querySelector("#compose-recipients").value;
    const subject = document.querySelector("#compose-subject").value;
    const body = document.querySelector("#compose-body").value;

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: recipients,
          subject: subject,
          body: body
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        // console.log(result);
    });

    load_mailbox("sent");

    return false;
  };

  // By default, load the inbox
  load_mailbox("inbox");
});



function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';


  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch_mailbox(mailbox);

}

function fetch_mailbox(mailbox) {

  fetch('/emails/' + mailbox)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      // console.log(emails);

      // ... do something else with emails ...
      emails.forEach(add_email)

  });
}



function add_email(contents) {

  // console.log(contents)

  const email = document.createElement('div');
  email.className = 'email-box';
  email.dataset.id = contents.id;
  

  const left_side = document.createElement('div');
  left_side.className = 'email-box__left-side'

  const sender = document.createElement('div');
  sender.innerHTML = contents.sender;

  const subject = document.createElement('div');
  subject.innerHTML = contents.subject;

  left_side.append(sender);
  left_side.append(subject);

  const timestamp = document.createElement('div');
  timestamp.innerHTML = contents.timestamp;


  email.append(left_side);
  email.append(timestamp);

  document.querySelector("#emails-view").append(email)
}