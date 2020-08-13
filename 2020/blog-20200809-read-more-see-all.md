# Read more

Isn't it annoying that on just about every website nowadays you have to click
the<span id="dots">...</span> <span onclick="ToggleState()" id="myBtn"
style="color:blue;cursor:pointer"><em>Read more</em></span> <span
id="readmore0">button? Just to see what comes next? It turns out next is just a
boring rant about some internet
[UX](https://en.wikipedia.org/wiki/User_experience) fad that is really
annoying. Nothing more. </span>

<span id="readmore1"> Arguably one of the more annoying offenders is [Audio
Technica](https://www.audio-technica.com). On any given product page, not just
do you have to click to expand the *Specifications* details. No, once you did
that, you also have to click a </span><span id="myBtn2"
onclick="ToggleState2()" style="color:blue;cursor:pointer"><em>See
all</em></span><span id="dots2">...</span><span id="readmore1.1"> button to
actually see enough of the specifications to be of any use.</span>

<span id="readmore2">
Why? Why, Audio Technica? What went wrong that you
implemented such an annoying feature? And where is the datasheet for the
product? Why is it hidden? Where is it hidden? Why I can I find a datasheet for
only half your products, and only by searching with Google or Duckduckgo.
</span>

<span id="readmore3">
Such [Read all]() expanding link-looking buttons have been around for a while,
and they are one of the most annoying features of online shopping. What went
wrong in the UX departments to invent and keep around such nonsense?
</span>

<span id="readmore4">
Showing walls of text is appalling to customers. So the obvious solution would
be to create useful and concise descriptions.
</span>

<span id="readmore5">
Is that what just about any online shop is doing? No. Instead, they just hide
the poorly written and overly lengthy descriptions! Ah, that must be the
explanation.
</span>

<span id="readmore5.8">
The</span><span id="dots3">...</span> <span id="myBtn3"
onclick="ToggleState3()" style="color:blue;cursor:pointer"><em>Read
more</em></span><span id="readmore5.9"> button is especially annoying when
there is not much more to read.
</span>

<span id="readmore6">
    < / rant id="clickmania">
</span>

<script language="JavaScript">
<!-- hide this script from old browsers
function ReadMoreChanger(newstate)
{
  var dots = document.getElementById("dots")
  var dots2 = document.getElementById("dots2")
  var dots3 = document.getElementById("dots3")
  var btnText = document.getElementById("myBtn")
  var btnText2 = document.getElementById("myBtn2")
  var btnText3 = document.getElementById("myBtn3")
  var moreText0 = document.getElementById("readmore0")
  var moreText1 = document.getElementById("readmore1")
  var moreText11 = document.getElementById("readmore1.1")
  var moreText2 = document.getElementById("readmore2")
  var moreText3 = document.getElementById("readmore3")
  var moreText4 = document.getElementById("readmore4")
  var moreText5 = document.getElementById("readmore5")
  var moreText58 = document.getElementById("readmore5.8")
  var moreText59 = document.getElementById("readmore5.9")
  var moreText6 = document.getElementById("readmore6")

  if (newstate === "first") {
    dots.style.display = "inline";
    dots2.style.display = "none";
    dots3.style.display = "none";
    btnText.innerHTML = "<em>Read more</em>";
    btnText2.style.display = "none";
    btnText3.style.display = "none";
    moreText0.style.display = "none";
    moreText1.style.display = "none";
    moreText11.style.display = "none";
    moreText2.style.display = "none";
    moreText3.style.display = "none";
    moreText4.style.display = "none";
    moreText5.style.display = "none";
    moreText58.style.display = "none";
    moreText59.style.display = "none";
    moreText6.style.display = "none";
  } else if (newstate === "second") {
    dots.style.display = "none";
    dots2.style.display = "inline";
    dots3.style.display = "none";
    btnText.innerHTML = "<em>read less</em>";
    btnText2.style.display = "inline";
    btnText2.innerHTML = "<em>See all</em>";
    btnText3.style.display = "none";
    moreText0.style.display = "inline";
    moreText1.style.display = "inline";
    moreText11.style.display = "none";
    moreText2.style.display = "none";
    moreText3.style.display = "none";
    moreText4.style.display = "none";
    moreText5.style.display = "none";
    moreText58.style.display = "none";
    moreText59.style.display = "none";
    moreText6.style.display = "none";
  } else if (newstate === "third") {
    dots.style.display = "none";
    dots2.style.display = "none";
    dots3.style.display = "inline";
    btnText.innerHTML = "<em>read less</em>";
    btnText2.style.display = "inline";
    btnText2.innerHTML = "<em>see less</em>";
    btnText3.style.display = "inline";
    btnText3.innerHTML = "<em>Read more</em>";
    moreText0.style.display = "inline";
    moreText1.style.display = "inline";
    moreText11.style.display = "inline";
    moreText2.style.display = "inline";
    moreText3.style.display = "inline";
    moreText4.style.display = "inline";
    moreText5.style.display = "inline";
    moreText58.style.display = "inline";
    moreText59.style.display = "none";
    moreText6.style.display = "none";
  } else { // see all
    dots.style.display = "none";
    dots2.style.display = "none";
    dots3.style.display = "none";
    btnText.innerHTML = "<em>read less</em>";
    btnText2.style.display = "inline";
    btnText2.innerHTML = "<em>see less</em>";
    btnText3.style.display = "inline";
    btnText3.innerHTML = "<em>read less</em>";
    moreText0.style.display = "inline";
    moreText1.style.display = "inline";
    moreText11.style.display = "inline";
    moreText2.style.display = "inline";
    moreText3.style.display = "inline";
    moreText4.style.display = "inline";
    moreText5.style.display = "inline";
    moreText58.style.display = "inline";
    moreText59.style.display = "inline";
    moreText6.style.display = "inline";
  }
}
function ToggleState() {
  var dots = document.getElementById("dots")
  var btnText2 = document.getElementById("myBtn2")
  var btnText3 = document.getElementById("myBtn3")
  var second = !(dots.style.display === "none");
  var third = (btnText2.innerHTML.includes("less"));
  var fourth = (btnText3.innerHTML.includes("less"));
  if (!second) {
    ReadMoreChanger("first");
  } else if (!third) {
    ReadMoreChanger("second");
  } else if (!fourth) {
    ReadMoreChanger("third");
  } else {
    ReadMoreChanger("all");
  }
}
function ToggleState2() {
  var dots2 = document.getElementById("dots2")
  var btnText3 = document.getElementById("myBtn3")
  var third = !(dots2.style.display === "none");
  var fourth = (btnText3.innerHTML.includes("less"));
  if (!third) {
    ReadMoreChanger("second");
  } else if (!fourth){
    ReadMoreChanger("third");
  } else {
    ReadMoreChanger("all");
  }
}
function ToggleState3() {
  var dots3 = document.getElementById("dots3")
  var fourth = !(dots3.style.display === "none");
  if (!fourth) {
    ReadMoreChanger("third");
  } else {
    ReadMoreChanger("all");
  }
}
function InitState() {
  ReadMoreChanger("first")
}
window.onload = InitState;
// done hiding from old browsers -->
</script>

