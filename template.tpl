%include('header.tpl')

	<div class="services-page main grid-wrap">

		<header class="grid col-full">
			<hr/>		
		</header>

		<aside class="grid col-one-quarter mq2-col-full">
			{{get('TOC', 'pas de TOC')}}
		
			<menu>
            <div id="menu">MENU</div>
			</menu>
		</aside>
		
		<section class="grid col-three-quarters mq2-col-full">
		
			<div class="grid-wrap">
			<article id="navbutton" class="grid col-full">

			{{get('CONTENT', 'pas de contenu')}} 

			</article>
			</div> 
		 <br/>
         <hr/>
         <!-- PAGE_TITLE  | LAST_CHANGE   TIME (RECENT_CHANGES ) |EDIT HELP HISTORY -->
		</section>    
	</div>

%include('foother.tpl')