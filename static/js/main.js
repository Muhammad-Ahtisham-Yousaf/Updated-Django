function showSidebar(){
    const sidebar = document.querySelector('.menu')
        sidebar.style.display = 'flex' 
    }
    
function hideSidebar(){
        const sidebar= document.querySelector('.menu')
        sidebar.style.display = 'none'
        
    }
// swiper
// <!-- Initialize Swiper -->
var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
  rotate: 50,
  stretch: 0,
  depth: 100,
  modifier: 1,
  slideShadows: true,
},
  pagination: {
el: ".swiper-pagination",
clickable: true,
},

  
});

// document.addEventListener('DOMContentLoaded', function() {
//     const filterSelects = document.querySelectorAll('.filter-select');
//     const chosenCards = document.querySelector('.filter-chosen');

//     filterSelects.forEach(function(filterSelect) {
//         filterSelect.addEventListener('change', function() {
//             const selectedOption = this.options[this.selectedIndex];
//             const selectedOptionText = selectedOption.textContent;
//             const selectedOptionValue = selectedOption.value;

//             if (selectedOptionValue) {
//                 const chosenCard = document.createElement('div');
//                 chosenCard.classList.add('chosen-card');
//                 chosenCard.textContent = selectedOptionText;

//                 const closeIcon = document.createElement('i');
//                 closeIcon.classList.add('fas', 'fa-times-circle');
//                 chosenCard.appendChild(closeIcon);

//                 closeIcon.addEventListener('click', function() {
//                     chosenCard.remove();
//                     filterSelect.selectedIndex = 0;
//                 });

//                 chosenCards.appendChild(chosenCard);
//             }
//         });
//     });
// });

const filterSelects = document.querySelectorAll('.filter-select');
const chosenCards = document.querySelector('.filter-chosen');

filterSelects.forEach(filterSelect => {
  filterSelect.addEventListener('change', () => {
    const selectedOptions = Array.from(filterSelect.options)
      .filter(option => option.selected)
      .map(option => option.textContent);

    const newChosenCard = document.createElement('div');
    newChosenCard.classList.add('chosen-card');
    newChosenCard.textContent = selectedOptions.join(', ');

    const closeIcon = document.createElement('i');
    closeIcon.classList.add('fas', 'fa-times-circle');
    newChosenCard.appendChild(closeIcon);

    closeIcon.addEventListener('click', () => {
      newChosenCard.remove();
      filterSelect.selectedIndex = 0;
    });

    chosenCards.appendChild(newChosenCard);
  });
});