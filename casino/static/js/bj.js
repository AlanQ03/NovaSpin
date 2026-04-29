const dealerRadios = document.querySelectorAll('input[name="dealerChoice"]');
const peterVideo = document.getElementById("peter-video");
const popeVideo = document.getElementById("pope-video");

function showDealer(dealer) {
    localStorage.setItem("selectedDealer", dealer);

    peterVideo.pause();
    popeVideo.pause();

    peterVideo.style.display = "none";
    popeVideo.style.display = "none";

    if (dealer === "pope") {
        popeVideo.style.display = "block";
        popeVideo.currentTime = 0;
    } else {
        peterVideo.style.display = "block";
        peterVideo.currentTime = 0;
    }
}

function getActiveVideo() {
        const dealer = localStorage.getItem("selectedDealer") || "peter";
        return dealer === "pope" ? popeVideo : peterVideo;
}

const savedDealer = localStorage.getItem("selectedDealer") || "peter";

const savedRadio = document.querySelector(`input[name="dealerChoice"][value="${savedDealer}"]`);
if (savedRadio) {
    savedRadio.checked = true;
}

showDealer(savedDealer);

dealerRadios.forEach(radio => {
    radio.addEventListener("change", function () {
        showDealer(this.value);
    });
});

document.querySelectorAll(".video-form, .hit-stand-form").forEach(form => {
    form.addEventListener("submit", function(event) {
        const clickedButton = event.submitter;

        if (clickedButton.value === "stand") {
            return;
        }

        event.preventDefault();

        let hiddenAction = form.querySelector('input[name="action"]');

        if (!hiddenAction) {
            hiddenAction = document.createElement("input");
            hiddenAction.type = "hidden";
            hiddenAction.name = "action";
            form.appendChild(hiddenAction);
        }

        hiddenAction.value = clickedButton.value;

        const activeVideo = getActiveVideo();
        activeVideo.currentTime = 0;
        activeVideo.playbackRate = 2;
        activeVideo.play();

        activeVideo.onended = function () {
            form.submit();
        };
    });
});