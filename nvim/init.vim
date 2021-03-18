let mapleader = ","

" Specify a directory for plugins
" - For Neovim: stdpath('data') . '/plugged'
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.local/share/nvim/plugged')
"Automatically executes filetype plugin indent on and syntax enable. You can revert the settings after the call. e.g. filetype indent off, syntax off, etc.
"
Plug 'scrooloose/nerdtree'  " Initialize plugin system

Plug 'scrooloose/nerdcommenter'

Plug 'christoomey/vim-tmux-navigator'

Plug 'bling/vim-airline'
Plug 'tomasr/molokai'
Plug 'bronson/vim-trailing-whitespace'

Plug 'mileszs/ack.vim'

Plug 'jiangmiao/auto-pairs'

Plug 'terryma/vim-multiple-cursors'
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'jackguo380/vim-lsp-cxx-highlight'

Plug 'vim-syntastic/syntastic'
Plug 'itchyny/vim-cursorword'

Plug 'apzelos/blamer.nvim'
Plug 'igankevich/mesonic'

Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && yarn install'  }
Plug 'jeetsukumaran/vim-buffergator'
Plug 'bling/vim-bufferline'

Plug 'severin-lemaignan/vim-minimap'
call plug#end()

let g:minimap_highlight='RedrawDebugComposed'

let g:minimap_width = 10
let g:minimap_auto_start = 1
let g:minimap_auto_start_win_enter = 1

set number
set hlsearch
set list
set mouse=a

set cursorline
set ruler
set backspace=indent,eol,start

set autowrite
set autoread

set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set smarttab
set autoindent
set scrolljump=-15

let g:blamer_enabled = 1
let g:blamer_prefix = ' > '
let g:blamer_template = '<committer> <summary>'
let g:blamer_date_format = '%d/%m/%y'
let g:blamer_delay = 200
highlight Blamer guifg=Red

let g:molokai_original = 1
colorscheme molokai

inoremap <F1> <Esc>
inoremap <C-x> <Esc>
nnoremap <C-x> :w<cr>

nnoremap j gj
nnoremap k gk

noremap <leader>a :NERDTreeToggle<cr>

noremap <leader><space> :nohlsearch<cr>

let g:multi_cursor_use_default_mapping=0 
 " Default mapping
 let g:multi_cursor_start_word_key      = '<C-d>'
 let g:multi_cursor_select_all_word_key = '<A-d>'
 let g:multi_cursor_start_key           = 'g<C-d>'
 let g:multi_cursor_select_all_key      = 'g<A-d>'
 let g:multi_cursor_next_key            = '<C-d>' 
 let g:multi_cursor_prev_key            = '<C-p>' 
 let g:multi_cursor_skip_key            = '<C-x>' 
 let g:multi_cursor_quit_key            = '<Esc>'

 " c++ syntax highlighting                        
let g:cpp_class_scope_highlight = 1              
let g:cpp_member_variable_highlight = 1          
let g:cpp_class_decl_highlight = 1

let g:syntastic_cpp_checkers = ['cpplint']       
let g:syntastic_c_checkers = ['cpplint']         
let g:syntastic_cpp_cpplint_exec = 'cpplint'     
 " The following two lines are optional. Configure it to your liking!
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

if executable('rg')
    let g:ackprg = '/bin/rg --vimgrep'
    nnoremap <leader>r :Ack! 
endif

nnoremap <leader><leader> :call ToggleQuickfix()<cr>
function ToggleQuickfix()
    for buffer in tabpagebuflist()
        if bufname(buffer) == ''
            cclose
            return
        endif
    endfor
    copen
endfunction

vmap <C-c> "+yi
vmap <C-x> "+c
vmap <C-v> c<ESC>"+p
imap <C-v> <C-r><C-o>+

