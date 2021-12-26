#!/usr/bin/ruby
# Скрипт для автоматизированного создания страниц статей
# для блога LinuxSovet
# (C) 2021 Михаил Linuxoid85 Краснов <linuxoid85@gmail.com>

require 'parseconfig'
require 'optparse'
require 'ostruct'

options = OpenStruct.new

OptionParser.new do |opt|
  opt.on('-p', '--page PAGE', 'Страница для генерации') { |o| options.page = o }
  opt.on('-h', '--header HEADER', 'Заголовок страницы') { |o| options.header = o }
  opt.on('-t', '--type TYPE', 'Тип страницы') { |o| options.type = o }
end.parse!

$conf = "conf.ini"
$time = Time.new
$page = options.page
$header = options.header
$type = options.type

def error(message)
    puts "\033[31m#{message}\033[0m"
end

def write(content, file)
    file = file + ".md"
    File.write(file, content, mode: 'a')
end

def main
    if File.exist?($conf)
        config = ParseConfig.new($conf)
    else
        error "Файла #{$conf} не существует!"
        exit 1
    end

    if File.exist?($page+'.md') and not File.new($page+'.md').stat.zero?
        File.write($page+'.md', '', mode: 'w')
    end

    if $type == "gallery"
        $page = config["path"] + "/gallery/" + $page
    else
        $page = config["path"] + "/stats/" + $page
    end

    author = config["author"]
    date = "#{$time.day}.#{$time.month}.#{$time.year} #{$time.hour}:#{$time.min}"

    write "# #{$header}\n", $page

    if $type == "article"
        write "\n[Статьи](/LinuxSovet/stats/stats.md)\n", $page
    
    elsif $type == "gallery"
        write "\n[Галерея](/LinuxSovet/gallery/README.md)\n", $page
        write "\n<a href='pic/*.png'><img src='pic/*.png' width='455' height='256'></a>\n", $page
    else
        write "\n[Статьи](/LinuxSovet/stats/stats.md)\n", $page
    end

    write "\n<pre>\n<strong>Автор:</strong> #{author}\n", $page
    write "<strong>Дата написания:</strong> #{date}\n</pre>\n\n", $page
end

main