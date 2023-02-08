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
        
        // read email
        mark_email_as_read(email.dataset.id)

        fetch_email_page(email.dataset.id)
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
  document.querySelector('#specific-email').style.display = 'none';


  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  fetch_mailbox(mailbox);

}




function fetch_mailbox(mailbox) {

  fetch('/emails/' + mailbox)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      console.log(emails);
      console.log("F")

      // ... do something else with emails ...
      emails.forEach(add_email)

  });
};

function add_email(contents) {
 

  console.log(contents)


  const email = document.createElement('div');
  email.className = 'email-box';
  email.dataset.id = contents.id

  if (contents.read) {
    email.style.backgroundColor = "rgb(200, 200, 200)"
  }
  

  const left_side = document.createElement('div');
  left_side.className = 'email-box__left-side'

  const sender = document.createElement('div');
  sender.innerHTML = contents.sender;
  sender.className = 'email-box__sender'

  const subject = document.createElement('div');
  subject.innerHTML = contents.subject;

  left_side.append(sender);
  left_side.append(subject);

  const timestamp = document.createElement('div');
  timestamp.innerHTML = contents.timestamp;


  email.append(left_side);
  email.append(timestamp);

  document.querySelector("#emails-view").append(email)
};





function fetch_email_page(email_id) {
  fetch('/emails/' + email_id, {
    method: 'GET'
  })
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      load_email_page(email)
  
      // ... do something else with email ...
  });
}

function load_email_page(email) {

    // Show the mailbox and hide other views
    document.querySelector('#specific-email').style.display = 'block';
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
  
    // Show the mailbox name
    document.querySelector('#emails-view').innerHTML = ``;
    document.querySelector('#specific-email').innerHTML = ``;
  
    const view = document.querySelector('#specific-email')

        const from = document.createElement('div')
        from.innerHTML = "<strong>From:</strong> " + email.sender

        const to = document.createElement('div')
        to.innerHTML = "<strong>To:</strong> " + email.recipients

        const subject = document.createElement('div')
        subject.innerHTML = "<strong>Subject:</strong> " + email.subject

        const timestamp = document.createElement('div')
        timestamp.innerHTML = "<strong>Timestamp:</strong> " + email.timestamp

        const id = document.createElement('div')
        id.innerHTML = "<strong>id:</strong> " + email.id
        const read = document.createElement('div')
        read.innerHTML = "<strong>read:</strong> " + email.read
        const archived = document.createElement('div')
        archived.innerHTML = "<strong>archived:</strong> " + email.archived

    view.append(from)
    view.append(to)
    view.append(subject)
    view.append(timestamp)

    view.append(id)
    view.append(read)
    view.append(archived)

    const reply = document.createElement('button')
    reply.innerHTML = 'Reply'
    reply.classList = "btn btn-sm btn-outline-primary"

    const line = document.createElement('hr')

    const body = document.createElement('div');
    body.innerHTML = email.body

    view.append(reply)
    view.append(line)
    view.append(body)
}






function mark_email_as_read(email_id) {
  fetch('/emails/' + email_id, {
    method: 'PUT',
    body: JSON.stringify({
        read: true
    })
  })
}