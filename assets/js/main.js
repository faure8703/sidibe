(function ($) {
	"use strict";
	
	/*----------------------------
    Responsive menu Active
    ------------------------------ */
	$(".mainmenu ul#primary-menu").slicknav({
		allowParentLinks: false,
		nestedParentLinks: false,
		closeOnClick: false,
		closedSymbol: '&#9656;',
		openedSymbol: '&#9662;',
		prependTo: '.responsive-menu',
	});
	
	/*----------------------------
    START - Menubar scroll animation
    ------------------------------ */
	jQuery(window).on('scroll', function() {
		if ($(this).scrollTop() > 10) {
			$('.header').addClass("sticky");
		} else {
			$('.header').removeClass("sticky");
		}
	});
	
	/*----------------------------
    START - Smooth scroll animation
    ------------------------------ */
	$('.mainmenu li a, .logo a,.slicknav_nav li a').on('click', function () {
		if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
		&& location.hostname == this.hostname) {
		  var $target = $(this.hash);
		  $target = $target.length && $target
		  || $('[name=' + this.hash.slice(1) +']');
		  if ($target.length) {
			var targetOffset = $target.offset().top;
			$('html,body')
			.animate({scrollTop: targetOffset}, 2000);
		   return false;
		  }
		}
	});
	
	/*----------------------------
    START - Scroll to Top
    ------------------------------ */
	$(window).on('scroll', function() {
		if ($(this).scrollTop() > 600) {
			$('.scrollToTop').fadeIn();
		} else {
			$('.scrollToTop').fadeOut();
		}
	});
	$('.scrollToTop').on('click', function () {
		$('html, body').animate({scrollTop : 0},2000);
		return false;
	});
	
	/*----------------------------
    START - Slider activation
    ------------------------------ */
	$('.screenshot-wrap').slick({
		autoplay: true,
		dots: true,
		autoplaySpeed: 1000,
		slidesToShow: 3,
		centerPadding: '20%',
		centerMode: true,
		prevArrow: '',
		nextArrow: '',
		responsive: [{

		  breakpoint: 992,
		  settings: {
			slidesToShow: 1,
			centerPadding: '33.3%'
		  }

		},{

		  breakpoint: 576,
		  settings: {
			slidesToShow: 1,
			centerPadding: '0'
		  }

		}]
	});
	
	var testimonialSlider = $('.testimonial-wrap');
	testimonialSlider.owlCarousel({
		loop:true,
		dots: true,
		mouseDrag: false,
		autoplay: false,
		autoplayTimeout:4000,
		nav: false,
		items: 1,
	});
	testimonialSlider.on("translate.owl.carousel", function(){
		$(".single-testimonial-box img, .author-rating").removeClass("animated zoomIn").css("opacity", "0");
	});
	testimonialSlider.on("translated.owl.carousel", function(){
		$(".single-testimonial-box img, .author-rating").addClass("animated zoomIn").css("opacity", "1");
	});
	testimonialSlider.on('changed.owl.carousel', function(property) {
		var current = property.item.index;
		var prevRating = $(property.target).find(".owl-item").eq(current).prev().find('.author-img').html();
		var nextRating = $(property.target).find(".owl-item").eq(current).next().find('.author-img').html();
		$('.thumb-prev .author-img').html(prevRating);
		$('.thumb-next .author-img').html(nextRating);
	});
	$('.thumb-next').on('click', function() {
		testimonialSlider.trigger('next.owl.carousel', [300]);
		return false;
	});
	$('.thumb-prev').on('click', function() {
		testimonialSlider.trigger('prev.owl.carousel', [300]);
		return false;
	});
	
	var heroSlider = $('.hero-area-slider');
	heroSlider.owlCarousel({
		loop:true,
		dots: false,
		autoplay: true,
		autoplayTimeout: 5000,
		nav: true,
		navText: ["<i class='icofont icofont-long-arrow-left'></i>", "<i class='icofont icofont-long-arrow-right'></i>"],
		items: 1,
		animateIn: 'fadeIn',
		animateOut: 'fadeOut',
		mouseDrag: true,
		touchDrag: true,
		responsive:{
			768:{
				mouseDrag: false,
				touchDrag: false,
			}
		}
	});
	
	/*----------------------------
	START - videos popup
	------------------------------ */
	$('.popup-youtube').magnificPopup({type:'iframe'});
	//iframe scripts
	$.extend(true, $.magnificPopup.defaults, {  
		iframe: {
			patterns: {
				//youtube videos
				youtube: {
					index: 'youtube.com/', 
					id: 'v=', 
					src: 'https://www.youtube.com/embed/%id%?autoplay=1' 
				}
			}
		}
	});
	
	/*----------------------------
    START - Counterup
    ------------------------------ */
	$('.counter').counterUp({
		delay: 20,
		time: 3000
	});
	
	/*----------------------------
    START - Video
    ------------------------------ */
	if($.fn.YTPlayer){
		$(".player").YTPlayer();
	}
	
	/*----------------------------
    START - Switcher animation
    ------------------------------ */
	$('#toggle-switcher').on('click', function(){
		if($(this).hasClass('open')){
			$(this).removeClass('open');
			$('#switch-style').animate({'right':'-232px'});
		}else{
			$(this).addClass('open');
			$('#switch-style').animate({'right':'0'});
		}
	});
	
	/*----------------------------
    START - Preloader
    ------------------------------ */
	jQuery(window).on('load', function(){
		jQuery("#preloader").fadeOut(500);
	});
	
	/*----------------------------
    START - WOW JS animation
    ------------------------------ */
	new WOW().init();

	/*----------------------------
    START - Contact Popup Modal (10s)
    ------------------------------ */
	$(function() {
		// Inject the popup HTML into the page if not already present
		if ($('#contact-popup-overlay').length === 0) {
			var popupHtml = [
				'<div id="contact-popup-overlay" class="contact-popup-overlay">',
				'  <div class="contact-popup-modal" role="dialog" aria-modal="true" aria-labelledby="contact-popup-title">',
				'    <button type="button" class="contact-popup-close" id="contact-popup-close" aria-label="Fermer">&times;</button>',
				'    <div class="contact-popup-header">',
				'      <div class="contact-popup-badge"><i class="fa fa-circle" style="color:#25d366;font-size:9px;vertical-align:middle;margin-right:4px;"></i> En ligne 24h/24</div>',
				'      <h3 id="contact-popup-title">Besoin d\'une Aide Immédiate ?</h3>',
				'      <p class="contact-popup-subtitle">Grand Maître Marabout Voyant SIDIBE Salifou</p>',
				'    </div>',
				'    <div class="contact-popup-body">',
				'      <p class="contact-popup-text">',
				'        Amour, retour d\'affection rapide, protection, chance, voyance du Fa ou déblocage...<br>',
				'        <strong>Échangez directement avec le Maître en toute discrétion.</strong>',
				'      </p>',
				'      <div class="contact-popup-actions">',
				'        <a href="https://wa.me/2290196873373?text=Bonjour%20Grand%20Ma%C3%AEtre%20SIDIBE%2C%20j%27ai%20besoin%20d%27une%20aide%20imm%C3%A9diate%20et%20d%27une%20consultation." class="contact-popup-btn btn-whatsapp" target="_blank" rel="noopener">',
				'          <i class="fa fa-whatsapp"></i> Écrire sur WhatsApp',
				'        </a>',
				'        <a href="tel:+2290196873373" class="contact-popup-btn btn-call">',
				'          <i class="fa fa-phone"></i> Appeler le +229 01 96 87 33 73',
				'        </a>',
				'      </div>',
				'      <div class="contact-popup-footer-note">',
				'        <i class="fa fa-lock"></i> Consultation 100% confidentielle &amp; réponse rapide',
				'      </div>',
				'    </div>',
				'  </div>',
				'</div>'
			].join('');
			$('body').append(popupHtml);
		}

		function openContactPopup() {
			$('#contact-popup-overlay').addClass('active');
		}

		function closeContactPopup() {
			$('#contact-popup-overlay').removeClass('active');
			sessionStorage.setItem('contact_popup_closed', '1');
		}

		// Show popup after 10 seconds (10000ms)
		setTimeout(function() {
			if (!sessionStorage.getItem('contact_popup_closed')) {
				openContactPopup();
			}
		}, 10000);

		// Event handlers for closing the popup
		$(document).on('click', '#contact-popup-close', function(e) {
			e.preventDefault();
			closeContactPopup();
		});

		$(document).on('click', '#contact-popup-overlay', function(e) {
			if ($(e.target).is('#contact-popup-overlay')) {
				closeContactPopup();
			}
		});

		$(document).on('keydown', function(e) {
			if (e.key === 'Escape' || e.keyCode === 27) {
				closeContactPopup();
			}
		});
	});

}(jQuery));