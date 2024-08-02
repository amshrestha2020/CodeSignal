You have a list conversations, in which each element is a conversation that is represented as an array of words. You need to create a chatbot that will complete a conversation that is currently in progress, currentConversation.

To do that, the chatbot must find the conversation from the given list that has the largest number of unique words that match with words from the currentConversation. If there are several conversations that match this condition, the chatbot should use the one that appears first in conversations. If no conversation from the list contains any matching words from currentCoversation, the chatbot should leave currentConversation as it is.

If there is a conversation that can complete currentConversation, the chatbot should find the first word in it that appears after all the matching words. The chatbot should then append this word, along with all the words that follow it in that conversation, to currentConversation.

Return the final state of currentConversation.

Example

For
conversations = [
    ["where", "are", "you", "live", "i", "live", "in", "new", "york"],
    ["are", "you", "going", "somewhere", "tonight", "no", "i", "am", "too", "tired", "today"],
    ["hello", "what", "is", "your", "name", "my", "name", "is", "john"]]
and currentConversation = ["hello", "john", "do", "you", "have", "a", "favorite", "city", "to", "live", "in", "yes", "it", "is"], the output should be
solution(conversations, currentConversation) = ["hello", "john", "do", "you", "have", "a", "favorite", "city", "to", "live", "in", "yes", "it", "is", "new", "york"].

The second conversation has only one matching word, "you". But the other two conversations both have three unique matching words. In the first conversation, the matches are "you", "live", and "in". In the third conversation, the matches are "hello", "john", and "is". Since we have two options that could complete our current conversation, we should choose the one that appears earlier in the list, so we use the first conversation. In that conversation, the last matching word is "in", so we add the last two words, "new" and "york", to currentConversation to complete it.

For
conversations = [
    ["lets", "have", "some", "fun"],
    ["i", "never", "get", "it"],
    ["be", "aware", "of", "this", "house"],
    ["he", "will", "call", "her"]]
and currentConversation = ["can", "you", "please"], the output should be
solution(conversations, currentConversation) = ["can", "you", "please"].

None of the conversations have any words that match words in currentConversation, so we add nothing to it.



def solution(conversations, currentConversation):
    def get_unique_matches(conv, curr_conv_set):
        return len(set(conv) & curr_conv_set)
    
    current_set = set(currentConversation)
    best_match_index = -1
    best_match_count = 0
    
    for i, conv in enumerate(conversations):
        unique_matches = get_unique_matches(conv, current_set)
        if unique_matches > best_match_count:
            best_match_count = unique_matches
            best_match_index = i
    
    if best_match_count == 0:
        return currentConversation
    
    best_conv = conversations[best_match_index]
    last_matching_word_index = -1
    
    for j, word in enumerate(best_conv):
        if word in current_set:
            last_matching_word_index = j
    
    if last_matching_word_index != -1 and last_matching_word_index < len(best_conv) - 1:
        currentConversation.extend(best_conv[last_matching_word_index + 1:])
    
    return currentConversation
