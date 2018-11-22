$(function(){
    smoothScroll(300);
    sliderBelt();
});

    function smoothScroll (duration){
        $('a[href^="#"]').on('click', function(event){
            var target = $( $(this).attr('href'));

            if (target.length) {
                event.preventDefault();
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, duration);
            }
        });
    }

    function sliderBelt(){
        $('.thumb-unit').click(function(){
            $('.slider-belt').css('left','-100%');
            $('.search-container').show();
        });

        $('.back').click(function(){
            $('.slider-belt').css('left','0%');
            $('.more-container').hide(700);
        });
    }

class TypedReactDemo extends React.Component {
  componentDidMount() {
    // If you want to pass more options as props, simply add
    // your desired props to this destructuring assignment.
    const { strings } = this.props;
    // You can pass other options here, such as typing speed, back speed, etc.
    const options = {
        strings: strings,
      typeSpeed: 50,
      backSpeed: 50
    };
    // this.el refers to the <span> in the render() method
    this.typed = new Typed(this.el, options);
  }

  componentWillUnmount() {
    // Make sure to destroy Typed instance on unmounting
    // to prevent memory leaks
    this.typed.destroy();
  }

  render() {
    return (
      <div className="wrap">
        <h1>Typed.js</h1>
        <div className="type-wrap">
          <span
            style={{ whiteSpace: 'pre' }}
            ref={(el) => { this.el = el; }}
          />
        </div>
        <button onClick={() => this.typed.toggle()}>Toggle</button>
        <button onClick={() => this.typed.start()}>Start</button>
        <button onClick={() => this.typed.stop()}>Stop</button>
        <button onClick={() => this.typed.reset()}>Reset</button>
        <button onClick={() => this.typed.destroy()}>Destroy</button>
      </div>
    );
  }
}

ReactDOM.render(
    <TypedReactDemo
    strings={[
        'Some <i>strings</i> are slanted',
      'Some <strong>strings</strong> are bold',
      'HTML characters &times; &copy;'
    ]}
  />,
  document.getElementById('react-root')
);

  //Change logo / profile pic
function(c) {
  var d = a(this),
    e = d.attr("href"),
    f = a(d.attr("data-target") || e && e.replace(/.*(?=#[^\s]+$)/, "")),
    g = f.data("bs.modal") ? "toggle" : a.extend({
      remote: !/#/.test(e) && e
    }, f.data(), d.data());
  d.is("a") && c.preventDefault(), f.one("show.bs.modal", function(a) {
    a.isDefaultPrevented() || f.one("hidden.bs.modal", function() {
      d.is(":visible") && d.trigger("focus")
    })
  }), b.call(f, g, this)
}