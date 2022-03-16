# Designing Your Career


This basically taken more or less verbatim from the [Design Your Postdoc Prework Assignment](https://app.smartsheet.com/b/publish?EQBCT=00e41b6655ec42f8ae0471cd6ea3e5d8). This prework assignment is required and must be filled out before the workshop. Save the result as a text file at the end.


## Uncover Your Needs


### Why are you here?

Please spend some time reflecting on the purpose of your work. Write a general
statement on your view:

*Why work?*

*What defines good work?*

*What do purpose, fulfillment, and growth have to do with it?*

*What might success and failure look like? What effect would success and failure have?*
</br>
<textarea id="content" rows="10" placeholder="Write something."></textarea>


### What are your goals?

Please spend some time brainstorming what you want to achieve.

*What do I want to do after my current situation ends? What are my career goals?*

*What things do I want to achieve while I'm here?*

*What milestones or deliverables will I need to get to my next step?*

*Are there any useful connections I should try to make (names or types of people)? How might I meet them?*

**I want to be a**
<br><input id="careergoal">

**I want to achieve/do:**
<br><input id="goals">

**Other milestones/deliverables I need:**
<br><input id="milestones">

**The people I want to meet include:**
<br><input id="peopletomeet">

**Other goals I have while still in the current position are:**
<br><input id="otherthings">


### What training do you need?

You might need some additional training in some areas. Maybe it is in writing,
public speaking, coding, time management, leadership, personal development,
specific skills, etc.
</br>
<textarea id="training" rows="5" placeholder="Awesome skillz."></textarea>


## What are your Values?

At the *Designing Your Postdoc* workshop they said that when people are
unhappiest, it is often linked to a disjuncture between their values and their
lives. So, what are your values?

Below is a list of values. Pick the ones most important to you. Don't think too
much about it but go by your gut.

Achievement. Advancement. Adventure. Autonomy. Basic Research. Clearly defined roles. Collective action. Community. Competition. Cooperation. Creativity. Cutting edge. Discovering new knowledge. Diversity. Elitism. Equality. Excellence. Excitement. Fairness. Family. Flexibility. Giving back. Harmony. Health. Helping. Impact. Inspiring the next generation. Integrity. Intellectual challenge. Learning. Location. Loyalty. Open communication. Passion. Prestige. Productivity. Recognition. Relationships. Respect. Service. Sharing knowledge. Stability. Structure. Success. Surroundings. Teamwork. Trust. Variety. Wealth.

Which of these are high priority values (up to 20)?
<br><textarea id="values" rows="3"></textarea>

Do you have other important values not listed?
<br><input id="valuesother">

What are your top 3-5 guiding values themes?
<br><input id="valuesguiding">


## Analyze Your Balance

In this workshop they did not talk about work-life balance. Instead, they say,
there are four things that need to be fulfilled to some extent: Love, Play,
Work, and Health. See this [video](https://www.youtube.com/watch?v=nJ6mi2ijCz8)
for an intro.


### What makes up your balance?

**Love** is what gives you a sense of connection. It can be fulfilled by friends,
family, and a community.
**Play** includes things you do for fun, e.g., your hobbies, music, and games.
**Work** is the stuff you do.
**Health** concerns your mind, body, and spirit. For example, what you eat, how you
exercise, and your spiritual practice.

What are the things that fill love for you?
<br><textarea id="lovethings" rows="2" placeholder="Love."></textarea>

What are the things that fill play for you?
<br><textarea id="playthings" rows="2" placeholder="Play."></textarea>

What are the things that fill work for you?
<br><textarea id="workthings" rows="2" placeholder="Work."></textarea>

What are the things that fill health for you?
<br><textarea id="healththings" rows="2" placeholder="Health."></textarea>


### How is your balance?

         |  |   |                                                                        |      |
-------- | - | - | ----------------------------------------------------------------------------- | ---------------------------
*Love*   |   | EMPTY | <input type="range" min="0" max="100" value="0" id="love">   | FULL | <span id="love_out"></span>
*Play*   |   | EMPTY | <input type="range" min="0" max="100" value="0" id="play">   | FULL | <span id="play_out"></span>
*Work*   |   | EMPTY | <input type="range" min="0" max="100" value="0" id="work">   | FULL | <span id="work_out"></span>
*Health* |   | EMPTY | <input type="range" min="0" max="100" value="0" id="health"> | FULL | <span id="health_out"></span>


### Maintain your balance

In order to maintain your balance in each of these areas, think about what you
can do to improve your balance or to rebalance when things go askew.

*What do you want to KEEP going forward?*
<br><input id="balance_keep">

*What do you want to CHANGE going forward?*
<br><input id="balance_change">

*What do you want to ADD going forward?*
<br><input id="balance_add">


## Identify Your Mentors, Explore Your Resources


### What mentorship do you need?


### What resources can you tap into?



## Save your work

<button onclick="saveFormAsTextFile()">Save to file</button>




<style type="text/css" media="screen">
  label textarea {vertical-align:top;}
  .slidecontainer { width: 100%; }
  input[type="range"] { width: 90; }
  input { width: 95%; }
  textarea { width: 100%; }
</style>

<script type="text/javascript">

function init_slider_output(v, vout) {
  var slider = document.getElementById(v);
  var output = document.getElementById(vout);
  output.innerHTML = slider.value;
  slider.oninput = function() {
    output.innerHTML = this.value;
  }
}
//init_slider_output('love', 'love_out');
//init_slider_output('play', 'play_out');
//init_slider_output('work', 'work_out');
//init_slider_output('health', 'health_out');


// https://gitlab.com/simongriffee/htmlformtofile
// Current date - http://stackoverflow.com/a/4929629/412329
var today = new Date();
var dd = today.getDate();
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();

if(dd<10) {
  dd='0'+dd
} 

if(mm<10) {
  mm='0'+mm
} 

today = yyyy+'-'+mm+'-'+dd;


function saveFormAsTextFile()
  // Based on https://thiscouldbebetter.wordpress.com/2012/12/18/loading-editing-and-saving-a-text-file-in-html5-using-javascrip/
{
  var textToSave =
    '# ' + today + '\n\n\n' +
    '## Why?\n\n' + document.getElementById('content').value + '\n\n\n' +
    '## Work-life balance\n\n' +
    'Love:   ' + document.getElementById('love').value + '\n' +
    'Play:   ' + document.getElementById('play').value + '\n' +
    'Work:   ' + document.getElementById('work').value + '\n' +
    'Health: ' + document.getElementById('health').value + '\n\n\n' +
    '## Values'

  var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
  var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
  var fileNameToSaveAs = today + '_design_your_career.md';

  var downloadLink = document.createElement("a");
  downloadLink.download = fileNameToSaveAs;
  downloadLink.innerHTML = "Download File";
  downloadLink.href = textToSaveAsURL;
  downloadLink.onclick = destroyClickedElement;
  downloadLink.style.display = "none";
  document.body.appendChild(downloadLink);

  downloadLink.click();
}

function destroyClickedElement(event)
{
  document.body.removeChild(event.target);
}
</script>
