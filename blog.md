---
layout: default
---


<aside class="sidebar">
  <header>
    <div class="about">
      <div class="cover-author-image">
        <a href="{{site.baseurl}}/"><img src="{{site.baseurl}}/assets/img/{% if site.author-img %}{{site.author-img}}{% endif %}" alt="{{site.author}}"></a>
      </div>
      <div class="author-name">{{site.author}}</div>
      <p>{{site.about-author}}</p>
    </div>

    <div class="buttons">
	<ul>
	<li><a href="../index.html">Home</a></li>
	<li><a href="">Research</a></li>
	</ul>
     </div>

  </header> <!-- End Header -->
  <footer>
    <section class="contact">
      <h3 class="contact-title">Contact me</h3>
      <ul>
        {% if site.social-twitter %}
          <li><a href="https://twitter.com/{{ site.social-twitter }}" target="_blank"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
        {% else %}
          <li><a href="https://twitter.com/artemsheludko_" target="_blank"><i class="fa fa-twitter" aria-hidden="true"></i></a></li>
        {% endif %}
        {% if site.social-facebook %}
          <li><a href="https://facebook.com/{{ site.social-facebook }}" target="_blank"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
        {% else %}
          <li><a href="https://facebook.com/" target="_blank"><i class="fa fa-facebook" aria-hidden="true"></i></a></li>
        {% endif %}
        {% if site.social-github %}
          <li class="github"><a href="http://github.com/{{site.social-github}}" target="_blank"><i class="fa fa-github"></i></a></li>
        {% else %}
          <li class="github"><a href="http://github.com/" target="_blank"><i class="fa fa-github" aria-hidden="true"></i></a></li>
        {% endif %}
        {% if site.social-linkedin %}
          <li class="linkedin"><a href="https://in.linkedin.com/in/{{site.social-linkedin}}" target="_blank"><i class="fa fa-linkedin"></i></a></li>
        {% else %}
          <li class="linkedin"><a href="https://in.linkedin.com/" target="_blank"><i class="fa fa-linkedin" aria-hidden="true"></i></a></li>
        {% endif %}
        {% if site.social-email %}
          <li class="email"><a href="mailto:{{site.social-email}}"><i class="fa fa-envelope-o"></i></a></li>
        {% else %}
          <li class="email"><a href="mailto:example.david@blog.com"><i class="fa fa-envelope-o" aria-hidden="true"></i></a></li>
        {% endif %}
      </ul>
    </section> <!-- End Section Contact -->
    <div class="copyright">
      <p>{{site.time | date: '%Y'}} &copy; {{site.author}}</p>
    </div>
  </footer> <!-- End Footer -->
</aside> <!-- End Sidebar -->
<div class="content-box clearfix">
  {{ content }}
</div>



{% for post in paginator.posts %}
<article class="post">
  {% if post.img %}
    <a class="post-thumbnail" style="background-image: url({{"/assets/img/" | prepend: site.baseurl | append : post.img}})" href="{{post.url | prepend: site.baseurl}}"></a>
  {% else %}
  {% endif %}
  <div class="post-content">
    <h2 class="post-title"><a href="{{post.url | prepend: site.baseurl}}">{{post.title}}</a></h2>
    <p>{{ post.content | strip_html | truncatewords: 15 }}</p>
    <span class="post-date">{{post.date | date: '%Y, %b %d'}}&nbsp;&nbsp;&nbsp;—&nbsp;</span>
    <span class="post-words">{% capture words %}{{ post.content | number_of_words }}{% endcapture %}{% unless words contains "-" %}{{ words | plus: 250 | divided_by: 250 | append: " minute read" }}{% endunless %}</span>
  </div>
</article>
{% endfor %}
