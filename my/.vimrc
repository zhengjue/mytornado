"source bundle plugin{
    "vundle start must required setup{
        set nocompatible
        filetype off
        set rtp+=~/.vim/bundle/vundle
        call vundle#begin()
        Plugin 'gmarik/vundle'
    "}
    "user Plug install{
        "Plugin 'klen/python-mode'
        ""code folding
        Plugin 'tmhedberg/SimpylFold' "折叠
        Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
        Plugin 'tpope/vim-fugitive' "git 支持
        Plugin 'scrooloose/nerdtree' "文件树目录
        Plugin 'jistr/vim-nerdtree-tabs'
        Plugin 'majutsushi/tagbar' "函数列表

	Plugin 'tomasr/molokai'
        Plugin 'jnurmine/Zenburn'
        Plugin 'altercation/vim-colors-solarized'

        Plugin 'Valloric/YouCompleteMe' "杀手级补全, clang级别的补全以及cache补全
        Plugin 'davidhalter/jedi-vim' "和上面配合的python 补全工具

        Plugin 'scrooloose/syntastic' "所有语言语法检查
	Plugin 'scrooloose/nerdcommenter' "快速添加取消注释
	Plugin 'hdima/python-syntax' "python 语法
	Plugin 'kevinw/pyflakes-vim' "python 语法检查
	Plugin 'tell-k/vim-autopep8' "对python文件自动pep8格式化
        Plugin 'nvie/vim-flake8' "支持pep8
        Plugin 'kien/ctrlp.vim' "杀手级, 重新定义了编辑器打开文件的方式
        Plugin 'tacahiroy/ctrlp-funky' "ctrlp增强工具
	Plugin 'Lokaltog/vim-easymotion'  "杀手级跳转
        Plugin 'vim-scripts/indentpython.vim' "python 高级缩进
    	Plugin 'SirVer/ultisnips' "快速插入代码片段snippets
    	Plugin 'honza/vim-snippets' "snippets模板
	Plugin 'kien/rainbow_parentheses.vim' "嵌套括号的美观匹配高亮
	Plugin 'Yggdroot/indentLine'  " 缩进虚线
	Plugin 'Raimondi/delimitMate' " 括号补全
	Plugin 'junegunn/vim-easy-align' "方便的按分隔符对齐,比如=号
	Plugin 'nathanaelkane/vim-indent-guides' "可视化的方式能将相同缩进的代码关联起来。 显可视化缩进,示对齐线
	Plugin 'bronson/vim-trailing-whitespace' "将代码行最后无效的空格标红

	Plugin 'vim-scripts/matchit.zip'
	"extended % matching for HTML, LaTeX, and many other languages
	Plugin 'terryma/vim-expand-region'
       	"allows you to visually select increasingly larger regions of text using the same key combination.
    "}

    "bundle end must required setup{
         call vundle#end()
         filetype plugin indent on
    "}
"}

"Bundle 'scrooloose/nerdcommenter'{
	let NERDSpaceDelims = 1
	""<leader>cc
	"注释当前选中文本，如果选中的是整行则在每行首添加 //，如果选中
	"一行的部分内容则在选中部分前后添加分别 /、/；
	"<leader>cu "取消选中文本块的注释。
"}

"'快速插入代码片段{
	"Bundle 'SirVer/ultisnips'
	"let g:UltiSnipsExpandTrigger = '<tab>'
	"let g:UltiSnipsJumpForwardTrigger = '<tab>'
	"let g:UltiSnipsJumpBackwardTrigger='<s-tab>'
	""'定义存放代码片段的文件夹 .vim/snippets下，使用自定义和默认的，将会的到全局，有冲突的会提示
	"let g:UltiSnipsSnippetDirectories=['snippets', 'bundle/ultisnips/UltiSnips']
"}

"main setting{
	let mapleader = ','
	let g:mapleader = ','
	nmap <leader>w :w!<cr> 快速保存
	noremap <c-c> :!python %<cr> 快速用python运行当前文件

	"按;键触发(ctrlp)
	"按f键触发(easymotion)的双字母跳转
	"按空格键切换注释(nerdcommenter)
	"按<leader>t侧边文件目录(nerdtree)
	"按<c-j>触发ultisnips补全
	"按<c-n>向下选择,按<c-p>向上选择

	" Use <leader>l to toggle display of whitespace
	nmap <leader>l :set list!<CR>
	"系统剪贴板
	set clipboard=unnamed
	" automatically change window's cwd to file's dir
	set autochdir
	set nu

	" PEP8
	au BufNewFile,BufRead *.py
	\ set tabstop=4
	\ set softtabstop=4
	\ set shiftwidth=4
	\ set textwidth=120
	\ set expandtab
	\ set autoindent
	\ set fileformat=unix

	au BufNewFile,BufRead *.js, *.html, *.css
	\ set tabstop=2
	\ set softtabstop=2
	\ set shiftwidth=2

	"indentpython.vim
	highlight BadWhitespace ctermbg=red guibg=red
	au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

	"utf-8
	set encoding=utf-8

	"hightlight all line
	let python_highlight_all=1
	syntax on
"}

"autopep8{
	autocmd FileType python map <buffer> <F3> :call Autopep8()<CR>
	"Number of spaces per indent level (default: 4)
	let g:autopep8_indent_size=2
"}

" Enable folding{
	set foldmethod=indent
	set foldlevel=99
	"set foldmethod=syntax
	" Enable folding with the spacebar
	nnoremap <space> za
	let g:SimpylFold_docstring_preview=1
"}

"highlight设置超长行长{
	augroup vimrc_autocmds
	autocmd FileType python highlight Excess ctermbg=DarkGrey guibg=Black
	autocmd FileType python match Excess /\%120v.*/
	autocmd FileType python set nowrap
	augroup END
"}

" Powerline setup{
	set guifont=PowerlineSymbols\Droid\ Sans\ Mono\ for\ Powerline\ Nerd\ Font\Complete\ 12
	set nocompatible
	set laststatus=2
	set t_Co=256
	set statusline+=%{fugitive#statusline()}
	let g:Powerline_symbols = 'fancy'
"}

" ctrlP setting{
    	let g:ctrlp_map = '<leader>p'
	let g:ctrlp_cmd = 'CtrlP'
	map <leader>f :CtrlPMRU<CR>
	let g:ctrlp_custom_ignore = {
	\ 'dir':  '\v[\/]\.(git|hg|svn|rvm)$',
	\ 'file': '\v\.(exe|so|dll|zip|tar|tar.gz|pyc)$',
	\ }
	let g:ctrlp_working_path_mode=0
	let g:ctrlp_match_window_bottom=1
	let g:ctrlp_max_height=15
	let g:ctrlp_match_window_reversed=0
	let g:ctrlp_mruf_max=500
	let g:ctrlp_follow_symlinks=1
"}

"ctrlp-funky{
	nnoremap <Leader>fu :CtrlPFunky<Cr>
	" narrow the list down with a word under cursor
	nnoremap <Leader>fU :execute 'CtrlPFunky ' . expand('<cword>')<Cr>
	let g:ctrlp_funky_syntax_highlight = 1
	let g:ctrlp_extensions = ['funky']
" }

"kien/rainbow_parentheses.vim{
	let g:rbpt_colorpairs = [
	\['brown',       'RoyalBlue3'],
	\['Darkblue',    'SeaGreen3'],
	\['darkgray',    'DarkOrchid3'],
	\['darkgreen',   'firebrick3'],
	\['darkcyan',    'RoyalBlue3'],
        \['darkred',     'SeaGreen3'],
        \['darkmagenta', 'DarkOrchid3'],
        \['brown',       'firebrick3'],
        \['gray',        'RoyalBlue3'],
        \['black',       'SeaGreen3'],
        \['darkmagenta', 'DarkOrchid3'],
        \['Darkblue',    'firebrick3'],
        \['darkgreen',   'RoyalBlue3'],
        \['darkcyan',    'SeaGreen3'],
        \['darkred',     'DarkOrchid3'],
        \['red',         'firebrick3'],
        \]
	let g:rbpt_max = 40
	let g:rbpt_loadcmd_toggle = 0
"}

"Bundle 'nathanaelkane/vim-indent-guides'{
	let g:indent_guides_enable_on_vim_startup = 0  " 默认关闭
	let g:indent_guides_guide_size            = 1  " 指定对齐线的尺寸
	let g:indent_guides_start_level 	  = 2  " 从第二层开始可视化显示缩进
	" ig 打开/关闭 vim-indent-guides
"}

"for show no user whitespaces{
	"Bundle 'bronson/vim-trailing-whitespace'
	map <leader><space> :FixWhitespace<cr>
	"+space去掉末尾空格
"}

"Nerrtree{
	"文件浏览
	map <F2> :NERDTreeToggle<CR>
	"ignore files in NERDTree
	let NERDTreeIgnore=['\.pyc$', '\~$']
"}

"Highlight current line{
	au WinLeave * set nocursorline nocursorcolumn
	au WinEnter * set cursorline cursorcolumn
	set cursorline cursorcolumn
	"hi CursorLine   cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
	hi CursorLine   cterm=NONE ctermbg=black ctermfg=grey guibg=darkred guifg=white
	"hi CursorColumn cterm=NONE ctermbg=darkred ctermfg=white guibg=darkred guifg=white
	hi CursorColumn cterm=NONE ctermbg=black ctermfg=grey guibg=darkred guifg=white
"}

"color seting1{{{
	"syntax enable
	"if has('gui_running')
	""    set background=light
	"     colorscheme solarized
	"else
	"     set background=dark
	"     "colorscheme Zenburn
	"     colorscheme molokai
	"endif
	""colorscheme solarized
	"let g:solarized_termcolors=256
	"call togglebg#map("<F5>")
"}}}

"color seting2{{{
	"solarized
	"let g:solarized_termcolors=256
	"let g:solarized_termtrans=1
	"let g:solarized_contrast='normal'
	"let g:solarized_visibility='normal'
	""molokai
	"let g:molokai_original = 1
	"" 配色方案
	"set background=dark
	"set t_Co=256
	"if has('gui_running')
	"	colorscheme solarized
	"	"colorscheme molokai
	"	"colorscheme phd
	"else
	"	"colorscheme solarized
	"	colorscheme molokai
	"	"colorscheme phd
	"endif
"}}}

" Tagbar{
	let g:tagbar_width=35
	let g:tagbar_autofocus=1
	nnoremap <F6> :TagbarToggle<CR>
"}

"split navigations{
	    set splitbelow
	    set splitright
	    nnoremap <C-J> <C-W><C-J>
	    nnoremap <C-K> <C-W><C-K>
	    nnoremap <C-L> <C-W><C-L>
	    nnoremap <C-H> <C-W><C-H>
"}

"YcmCompleter{
	    let g:ycm_autoclose_preview_window_after_completion=1
	    "map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
	    set completeopt=longest,menu    "让Vim的补全菜单行为与一般IDE一致(参考VimTip1228)
	    autocmd InsertLeave * if pumvisible() == 0|pclose|endif "离开插入模式后自动关闭预览窗口
	    inoremap <expr> <CR>       pumvisible() ? "\<C-y>" : "\<CR>"    "回车即选中当前项
	    "上下左右键的行为 会显示其他信息
	    inoremap <expr> <Down>     pumvisible() ? "\<C-n>" : "\<Down>"
	    inoremap <expr> <Up>       pumvisible() ? "\<C-p>" : "\<Up>"
	    inoremap <expr> <PageDown> pumvisible() ? "\<PageDown>\<C-p>\<C-n>" : "\<PageDown>"
	    inoremap <expr> <PageUp>   pumvisible() ? "\<PageUp>\<C-p>\<C-n>" : "\<PageUp>"
	    "youcompleteme  默认tab  s-tab 和自动补全冲突
	    "let g:ycm_key_list_select_completion=['<c-n>']
	    let g:ycm_key_list_select_completion = ['<Down>']
	    "let g:ycm_key_list_previous_completion=['<c-p>']
	    let g:ycm_key_list_previous_completion = ['<Up>']
	    let g:ycm_confirm_extra_conf=0 "关闭加载.ycm_extra_conf.py提示
	    "
	    let g:ycm_collect_identifiers_from_tags_files=1    " 开启 YCM
	    "基于标签引擎
	    let g:ycm_min_num_of_chars_for_completion=2
	    "从第2个键入字符就开始罗列匹配项
	    let g:ycm_cache_omnifunc=0 " 禁止缓存匹配项,每次都重新生成匹配项
	    let g:ycm_seed_identifiers_with_syntax=1   " 语法关键字补全
	    nnoremap <F4> :YcmForceCompileAndDiagnostics<CR>
	    "force recomile with syntastic
	    ""nnoremap <leader>lo :lopen<CR>    "open locationlist
	    "nnoremap <leader>lc :lclose<CR>    "close locationlist
	    inoremap <leader><leader> <C-x><C-o>
	    ""在注释输入中也能补全
	    let g:ycm_complete_in_comments = 1
	    "在字符串输入中也能补全
	    let g:ycm_complete_in_strings = 1
	    ""注释和字符串中的文字也会被收入补全
	    let g:ycm_collect_identifiers_from_comments_and_strings = 0
	    nnoremap <leader>g :YcmCompleter GoToDefinitionElseDeclaration<CR>
	    " 跳转到定义处
	    let g:ycm_global_ycm_extra_conf="~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py"
	    let g:ycm_seed_identifiers_with_syntax=1    " 语法关键字补全
"}

"syntastic setting{
	    let g:syntastic_check_on_open=1
	    let g:syntastic_html_tidy_ignore_errors=[" proprietary attribute \"ng-"]
	    let g:syntastic_always_populate_loc_list = 1
	    let g:syntastic_auto_loc_list = 1
	    let g:syntastic_check_on_wq = 0
	    let g:syntastic_ignore_files=[".*\.py$"]
	    set statusline+=%#warningmsg#
	    set statusline+=%{SyntasticStatuslineFlag()}
	    set statusline+=%*
"}

"jedi-vim{{{
	    let g:jedi#auto_initialization = 1
	    let g:jedi#auto_vim_configuration = 1
	    let g:jedi#use_tabs_not_buffers = 1
	    let g:jedi#use_splits_not_buffers = "left"
	    let g:jedi#popup_on_dot = 1

	    let g:jedi#popup_select_first = 1

	    let g:jedi#show_call_signatures = "1"
	    let g:jedi#goto_command = "d"

	    let g:jedi#goto_assignments_command = "g"
	    let g:jedi#goto_definitions_command = ""
	    let g:jedi#documentation_command = "K"
	    let g:jedi#usages_command = "n"
	    let g:jedi#completions_command = ""
	    let g:jedi#rename_command = "r"

	    let g:jedi#completions_enabled = 1
"}}}


"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF

"Run pythoon
au BufRead *.py map <buffer> <F10> :w<CR>:!/usr/bin/env python % <CR>

"kevinw/pyflakes-vim
let g:pyflakes_use_quickfix = 1
