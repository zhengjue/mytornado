"source bundle plugin{
    "vundle start must required setup{
        set nocompatible
        filetype off
        set rtp+=~/.vim/bundle/vundle
        call vundle#begin()
        Plugin 'gmarik/vundle'
    "}
    "user Plug install{
        Plugin 'klen/python-mode'
        ""code folding
        Plugin 'tmhedberg/SimpylFold'
        Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
        Plugin 'tpope/vim-fugitive'
        Plugin 'scrooloose/nerdtree'
        Plugin 'jistr/vim-nerdtree-tabs'
        Plugin 'davidhalter/jedi-vim'
        Plugin 'majutsushi/tagbar'
        Plugin 'jnurmine/Zenburn'
        Plugin 'altercation/vim-colors-solarized'
        Plugin 'Valloric/YouCompleteMe'
        Plugin 'scrooloose/syntastic'
        Plugin 'nvie/vim-flake8'
        Plugin 'kien/ctrlp.vim'
        Bundle 'tacahiroy/ctrlp-funky'
        Plugin 'vim-scripts/indentpython.vim'
	Plugin 'SirVer/ultisnips'
	Plugin 'honza/vim-snippets'
    "}

    "bundle end must required setup{ 
         call vundle#end()
         filetype plugin indent on
    "}
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


"Other setting{
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
	     au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

	     "utf-8
	     set encoding=utf-8
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

"color seting{{{
       syntax enable
       if has('gui_running')
       "    set background=light
       colorscheme solarized
       "else
       "    set background=dark
       "	colorscheme Zenburn
       endif                                                              
       "colorscheme solarized                                                                                                        
       let g:solarized_termcolors=256                                     
       call togglebg#map("<F5>")                                          
"}}} 
"

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

"python-mode{
     "2 python mode seting{
         "2.1 common function{
            "Turn on the whole plugin  
            let g:pymode = 1
            "Turn off plugin's warnings  
            let g:pymode_warnings = 1
            "Add paths to `sys.path`,Value is list of path's strings. 
            let g:pymode_paths = []
            "Trim unused white spaces on save 
            let g:pymode_trim_whitespaces = 1
            "Setup default python options     
            let g:pymode_options = 1
            "Setup max line length 
            let g:pymode_options_max_line_length = 120
            "Enable colorcolumn display at max_line_length 
            let g:pymode_options_colorcolumn = 1
            "Setup pymode |quickfix| window
            let g:pymode_quickfix_minheight = 3
            let g:pymode_quickfix_maxheight = 6
         "} 
         
         "2.2 Python version{
            "Values are `python`, `python3`, `disable`. If value set to `disable` most python-features of **pymode** will be disabled. Set value to `python3` if you are working with python3 projects. You could use |exrc|
            let g:pymode_python = 'python' 
         "} 

         "2.3 Python indentation{
            "Enable pymode indentation 
            let g:pymode_indent = 1
         "} 

         "2.4 Python folding{
            "Enable pymode folding  
            let g:pymode_folding = 1
         "}

         "2.5 Vim motion{
              "`C` — means class
              "`M` — means method or function
              "================  ============================
              "Key               Command
              "================  ============================
              "[[                Jump to previous class or function (normal, visual, operator modes)
              "]]                Jump to next class or function  (normal, visual, operator modes)
              "[M                Jump to previous class or method (normal, visual, operator modes)
              "]M                Jump to next class or method (normal, visual, operator modes)
              "aC                Select a class. Ex: vaC, daC, yaC, caC (normal, operator modes)
              "iC                Select inner class. Ex: viC, diC, yiC, ciC (normal, operator modes)
              "aM                Select a function or method. Ex: vaM, daM, yaM, caM (normal, operator modes)
              "iM                Select inner function or method. Ex: viM, diM, yiM, ciM (normal, operator modes)
              "================  ============================
              "
            "Enable pymode-motion  
            let g:pymode_motion = 1
         "} 

         "2.6 Show documentation{
            "Commands:
            "	*:PymodeDoc* <args> — show documentation 
            "Turns on the documentation script 
            let g:pymode_doc = 1
            "Bind keys to show documentation for current word (selection)
            let g:pymode_doc_bind = 'K'
         "}

         "2.6 Support virtualenv{
            "Commands:
            "	*:PymodeVirtualenv* <path> -- Activate virtualenv (path is related to
            "	current working directory)
            "Enable automatic virtualenv detection  
            let g:pymode_virtualenv = 1
            "Set path to virtualenv manually 
            let g:pymode_virtualenv_path = $VIRTUAL_ENV
         "}
          
         "2.7 Run code{
            "Commands:
            "	*:PymodeRun* -- Run current buffer or selection
            "Turn on the run code script
            let g:pymode_run = 1
            "Binds keys to run python code
            let g:pymode_run_bind = '<Leader>r'
            au BufRead *.py map <buffer> <F10> :w<CR>:!/usr/bin/env python % <CR>
         "} 

         "2.8 Breakpoints {
            "Enable functionality  
            let g:pymode_breakpoint = 1
            "Bind keys
            let g:pymode_breakpoint_bind = '<Leader>b'
            "Manually set breakpoint command (leave empty for automatic detection)
            let g:pymode_breakpoint_cmd = ''
         "} 
     "}

     "3 Code checking{
        "3.0 Turn on code checking{
            let g:pymode_lint = 1

            "Check code on every save (if file has been modified)  *'g:pymode_lint_on_write'*
            let g:pymode_lint_on_write = 1

            "Check code on every save (every)
            let g:pymode_lint_unmodified = 0

            "Check code when editing (on the fly)                       
            let g:pymode_lint_on_fly = 0

            "Show error message if cursor placed at the error line 
            let g:pymode_lint_message = 1

            "Default code checkers (you could set several)      
            "Values may be chosen from: `pylint`, `pep8`, `mccabe`, `pep257`, `pyflakes`.
            let g:pymode_lint_checkers = ['pyflakes', 'pep8', 'mccabe']
              
            "Skip errors and warnings                 
            "E.g. "E501,W002", "E2,W" (Skip all Warnings and Errors that starts with E2) and etc
            let g:pymode_lint_ignore = "E501,W"

            "Select some error or warnings.          
            "By example you disable all warnings starting from 'W', but want to see warning
            "'W0011' and warning 'W430'
            let g:pymode_lint_select = "E501,W0011,W430"

            "Sort errors by relevance      
            "If not empty, errors will be sort by defined relevance
            "E.g. let g:pymode_lint_sort = ['E', 'C', 'I']  " Errors first 'E',
            "after them 'C' and ...
            let g:pymode_lint_sort = []

            "Auto open cwindow (quickfix) if any errors have been found
            let g:pymode_lint_cwindow = 1

            "Place error |signs|          
            let g:pymode_lint_signs = 1

            "Definitions for |signs|
            let g:pymode_lint_todo_symbol = 'WW'
            let g:pymode_lint_comment_symbol = 'CC'
            let g:pymode_lint_visual_symbol = 'RR'
            let g:pymode_lint_error_symbol = 'EE'
            let g:pymode_lint_info_symbol = 'II'
            let g:pymode_lint_pyflakes_symbol = 'FF'
        "}

        "3.1 Set code checkers options{
            "Set PEP8 options
            let g:pymode_lint_options_pep8 ={'max_line_length': g:pymode_options_max_line_length}
            "Set Pyflakes options 
            let g:pymode_lint_options_pyflakes = { 'builtins': '_' }
            "Set mccabe options 
            let g:pymode_lint_options_mccabe = { 'complexity': 12 }
            "Set pep257 options      
            let g:pymode_lint_options_pep257 = {}
            "Set pylint options 
            let g:pymode_lint_options_pylint ={'max-line-length': g:pymode_options_max_line_length}
        "}

        "3.2 Rope support ~{
            "Pymode supports Rope refactoring operations, code completion and code assists.

            "Commands:
              "|:PymodeRopeAutoImport| -- Resolve import for element under cursor
              "|:PymodeRopeModuleToPackage| -- Convert current module to package
              "|:PymodeRopeNewProject| -- Open new Rope project in current working directory
              "|:PymodeRopeRedo| -- Redo changes from last refactoring
              "|:PymodeRopeRegenerate| -- Regenerate the project cache
              "|:PymodeRopeRenameModule| -- Rename current module
              "|:PymodeRopeUndo| -- Undo changes from last refactoring

            "Turn on the rope script 
            let g:pymode_rope = 0

            "Enable searching for |.ropeproject| in parent directories
            let g:pymode_rope_lookup_project = 0

            "You can also manually set the rope project directory. If not specified rope will use the current directory.
            let g:pymode_rope_project_root = ""

            let g:pymode_rope_ropefolder='.ropeproject'

            "Leave empty to disable the key binding
            let g:pymode_rope_show_doc_bind = '<C-c>d'

            "Regenerate project cache on every save (if file has been modified)
            let g:pymode_rope_regenerate_on_write = 1
         "}
     "}
    
     "4 auto complete seting{
        "4.1 Completion{
            "Turn on code completion support in the 
            let g:pymode_rope_completion = 0

            "Turn on autocompletion when typing a period
            let g:pymode_rope_complete_on_dot = 1

            "Keymap for autocomplete                        
            let g:pymode_rope_completion_bind = '<C-Space>'

            "Extended autocompletion (rope could complete objects which have not been imported) from project 
            let g:pymode_rope_autoimport = 1

            "Load modules to autoimport by default     
            let g:pymode_rope_autoimport_modules = ['os', 'shutil', 'datetime']

            "Offer to unresolved import object after completion.
            let g:pymode_rope_autoimport_import_after_complete = 1
        "}

        "4.2 Find definition {
            "By default when you press *<C-C>g* on any object in your code you will be moved to definition

            "Leave empty for disable key binding.
            let g:pymode_rope_goto_definition_bind = '<C-c>g'

            "Command for open window when definition has been found
            "Values are (`e`, `new`, `vnew`)
            let g:pymode_rope_goto_definition_cmd = 'new'
        "}

        "4.3 Refactoring{
            "Keymap for rename method/function/class/variables under cursor
            let g:pymode_rope_rename_bind = '<C-c>rr'

            "Rename a current module/package 
            "Keymap for rename current module 
            let g:pymode_rope_rename_module_bind = '<C-c>r1r'

            let g:pymode_rope_organize_imports_bind = '<C-c>ro'

            "Insert import for current word under cursor    *'g:pymode_rope_autoimport_bind'*
            "Should be enabled |'g:pymode_rope_autoimport'|
            let g:pymode_rope_autoimport_bind = '<C-c>ra'

            "Convert module to package ~
            "Keybinding:
            let g:pymode_rope_module_to_package_bind = '<C-c>r1p'

            "Extract method/variable ~
            let g:pymode_rope_extract_method_bind = '<C-c>rm'
            let g:pymode_rope_extract_variable_bind = '<C-c>rl'

            "Use function ~
            let g:pymode_rope_use_function_bind = '<C-c>ru'

            "Move method/fields ~
            let g:pymode_rope_move_bind = '<C-c>rv'

            "Change function signature 
            let g:pymode_rope_change_signature_bind = '<C-c>rs'
        "}

        "4.4 Undo/Redo changes {
            "Commands:
            "*:PymodeRopeUndo* -- Undo last changes in the project
            "*:PymodeRopeRedo* -- Redo last changes in the projec
        "}
     "} 
     
     "5. Syntax{ ~
            "Turn on pymode syntax   
            let g:pymode_syntax = 1

            "Slower syntax synchronization that is better at handling code blocks in
            "docstrings. Consider disabling this on slower hardware
            let g:pymode_syntax_slow_sync = 1


            "Enable all python highlights    
            let g:pymode_syntax_all = 1

            "Highlight "print" as a function   
            let g:pymode_syntax_print_as_function = 1

            "Highlight "async/await" keywords    
            let g:pymode_syntax_highlight_async_await = g:pymode_syntax_all

            "Highlight '=' operator 
            let g:pymode_syntax_highlight_equal_operator = g:pymode_syntax_all

            "Highlight '*' operator  
            let g:pymode_syntax_highlight_stars_operator = g:pymode_syntax_all

            "Highlight 'self' keyword 
            let g:pymode_syntax_highlight_self = g:pymode_syntax_all

            "Highlight indent's errors  
            let g:pymode_syntax_indent_errors = g:pymode_syntax_all

            "Highlight space's errors    
            let g:pymode_syntax_space_errors = g:pymode_syntax_all

            "Highlight string formatting 
            let g:pymode_syntax_string_formatting = g:pymode_syntax_all
            let g:pymode_syntax_string_format = g:pymode_syntax_all
            let g:pymode_syntax_string_templates = g:pymode_syntax_all
            let g:pymode_syntax_doctests = g:pymode_syntax_all


            "Highlight builtin objects (True, False, ...)
            let g:pymode_syntax_builtin_objs = g:pymode_syntax_all

            "Highlight builtin types (str, list, ...) 
            let g:pymode_syntax_builtin_types = g:pymode_syntax_all

            "Highlight exceptions (TypeError, ValueError, ...) 
            let g:pymode_syntax_highlight_exceptions = g:pymode_syntax_all

            "Highlight docstrings as pythonDocstring (otherwise as pythonString)
            let g:pymode_syntax_docstrings = g:pymode_syntax_all
     "}
"}

"jedi-vim{
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
"}


"python with virtualenv support
py << EOF
import os
import sys
if 'VIRTUAL_ENV' in os.environ:
    project_base_dir = os.environ['VIRTUAL_ENV']
    activate_this = os.path.join(project_base_dir, 'bin/activate_this.py')
    execfile(activate_this, dict(__file__=activate_this))
EOF
