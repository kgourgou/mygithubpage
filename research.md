---
layout: base
---

<div class="wrapper">
    <header>
        {% if site.compass.logo %}
        <div class="logo-container">
          <a class="logo" href="{{ page.baseurl }}" style="background-image: url('{{ site.baseurl }}{{ site.compass.logo }}')"></a>
        </div>
        {% endif %}

        {% if site.compass.author %}
        <div class="author-container"><h1>{{ site.compass.author }}</h1></div>
        {% endif %}

        <div class="icon-container">
          <a href="mailto:kgourgoulias+mywebsite@gmail.com"><i class="fa fa-envelope fa-2x"></i></a>

          <a href="https://github.com/kgourgou"><i class="fa fa-github fa-2x"></i></a>

          <a  href="https://twitter.com/kgourg"><i class="fa fa-twitter fa-2x"></i></a>

          <a href="https://www.linkedin.com/in/kgourgoulias"><i class="fa fa-linkedin fa-2x"></i></a>

        </div>

        {% if site.compass.tagline %}
        <div class="tagline-container"><p>{{ site.compass.tagline }}</p></div>
        {% endif %}

    </header>
    <main>
    <a href="../index.html"><i class="fa fa-arrow-circle-o-left fa-2x">BACK</i></a>

    
     # My Research

    ## Publications

    * *Information metrics for long-time errors in splitting schemes for stochastic dynamics and parallel kMC*, with Markos A. Katsoulakis and Luc Rey-Bellet. [[ArXiv]](http://arxiv.org/abs/1511.08240)


    * *Metrics for irreversibility of splitting schemes in parallel kMC*, with Markos A. Katsoulakis and Luc Rey-Bellet (In preparation, title may change).
    </main>
</div>



