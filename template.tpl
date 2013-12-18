% include('header.tpl', title='Page Title')

	<div class="services-page main grid-wrap">

		<header class="grid col-full">
			<hr/>		
		</header>

		<aside class="grid col-one-quarter mq2-col-full">
			{{get('TOC', ''}}
		
			<menu>
            {<div id="menu">MENU</div>}
			</menu>
		</aside>
		
		<section class="grid col-three-quarters mq2-col-full">
		
			<div class="grid-wrap">
			<article id="navbutton" class="grid col-full">


				{{CONTENT or ''}}
					
			
			</article>
			</div> <!-- 100%articles-->
		 <br/>
         <hr/>
         {{PAGE_TITLE or ''}} | {{LAST_CHANGE  or ''}} {{TIME or ''}} ({{RECENT_CHANGES or ''}}) |{{EDIT or ''}} {{(HELP or '')}} {{HISTORY or ''}}
		</section>	
		       
	</div> <!--main-->

% include('foother.tpl')

