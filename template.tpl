%include('header.tpl')

	<div class="services-page main grid-wrap">

		<header class="grid col-full">
			<hr/>		
		</header>

		<aside class="grid col-one-quarter mq2-col-full">

		% if ACTION != 'edit':

			{{get('TOC', 'pas de TOC')}}
		
			<menu>
            <div id="menu">MENU</div>
			</menu>
		%end
		</aside>
		
		<section class="grid col-three-quarters mq2-col-full">
		
			<div class="grid-wrap">
			<article id="navbutton" class="grid col-full">

			% if defined('ERROR'):
				<div class="error">{{ERROR}}</div>
				<hr/>
			% end

			% if ACTION == 'edit':

			<form method="post" action="./save">
				<textarea name="content" cols="83" rows="30" style="width: 100%;">

				{{!CONTENT if CONTENT else "No content"}}
				</textarea>
				<input type="hidden" name="page" value="Projets" /><br/>
				<p align="right">Mot de passe : <input type="password" name="password"/>
					<input type="submit" value="Enregistrer" accesskey="s" />
				</p>
			</form>

			% else:					
				{{!CONTENT if CONTENT else "No content"}}

			% end

			</article>
			</div> 
		 <br/>
         <hr/>
         <a href="/{{PAGE_NAME}}/edit">Éditer</a>
         <!-- PAGE_TITLE  | LAST_CHANGE   TIME (RECENT_CHANGES ) |EDIT HELP HISTORY -->
		</section>    
	</div>

%include('foother.tpl')