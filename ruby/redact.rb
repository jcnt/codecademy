puts "type in some text"
text = gets.chomp
puts "words to redact"
redact = gets.chomp

words = text.split(" ")
red = redact.split(" ")

#NEEDFIX

words.each do |word|
    red.each do |reda|
        if word == reda
            print "REDACTED "
            next
            next
        end
        print word + " "
    end
end


